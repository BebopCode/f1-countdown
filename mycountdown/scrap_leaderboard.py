from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timezone
import pytz
import os 
import django
from django.utils import timezone
import json
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mycountdown.settings')
django.setup()
from scrap.models import RaceModel, LeaderBoard

gmt_offset_str = None

def convert_string_to_datetime(date_str):
    naive_datetime = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
    sign = 1 if gmt_offset_str[0] == '+' else -1
    hours_offset = int(gmt_offset_str[1:3])  
    minutes_offset = int(gmt_offset_str[4:]) 


    total_minutes_offset = sign * (hours_offset * 60 + minutes_offset)
    timezone = pytz.FixedOffset(total_minutes_offset)
    aware_datetime = timezone.localize(naive_datetime)
    return aware_datetime

def scrape():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.binary_location = "/usr/bin/chromium-browser"

    driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
    driver.get("https://www.formula1.com/en/results.html/2024/drivers.html")
    tbody = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "tbody"))
    )
    rows = tbody.find_elements(By.TAG_NAME, "tr")

# Initialize a list to store the data
    data = []

    # Iterate through each row
    for row in rows:
    # Find all td elements in the row
        cells = row.find_elements(By.TAG_NAME, "td")

        # Check if the row has exactly 5 td elements
        
        #Extract text from each cell
        row_data = [cell.text for cell in cells]
        
        # Create a# dictionary for the row
        row_dict = {
            "Position": row_data[1],
            "Driver": row_data[2],
            "Car": row_data[4],
            "Points": row_data[5]
        }
        
        # Add the row dictionary to the data list
        data.append(row_dict)

    # Save the data to a JSON file
    with open("driver_standings.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Data saved to driver_standings.json")
    driver.quit()
    LeaderBoard.objects.all().delete()
    for driver in data:
        driver_model_data = LeaderBoard(
            update_time = timezone.now(),
            position = driver["Position"],
            driver = driver["Driver"],
            car = driver["Car"],
            points = driver["Points"],
            )
        driver_model_data.save()

    all_race_data = LeaderBoard.objects.all()
    print(len(all_race_data))
    

if __name__ =="__main__":
    scrape()

