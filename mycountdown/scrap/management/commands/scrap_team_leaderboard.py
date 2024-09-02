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
from scrap.models import TeamLeaderBoard
from django.core.management.base import BaseCommand
gmt_offset_str = None

class Command(BaseCommand):
    def scrape(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        #chrome_options.binary_location = "/usr/bin/chromium-browser"

        driver = webdriver.Chrome(options = chrome_options)  # Optional argument, if not specified will search path.
        driver.get("https://www.formula1.com/en/results.html/2024/team.html")
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
            print(row_data)
            # Create a# dictionary for the row
            row_dict = {
                "Position": row_data[0],
                "Team": row_data[1],
                "Points": row_data[2]
            }
            
            # Add the row dictionary to the data list
            data.append(row_dict)

        # Save the data to a JSON file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        print(current_dir)
        json_file_path = os.path.join(current_dir, 'team_standings.json')
        with open(json_file_path, "w") as f:
            json.dump(data, f, indent=4)

        print("Data saved to team_standings.json")
        driver.quit()
        TeamLeaderBoard.objects.all().delete()
        for team in data:
            team_model_data = TeamLeaderBoard(
                update_time = timezone.now(),
                position = team["Position"],
                team = team["Team"],
                points = team["Points"],
                )
            team_model_data.save()

        all_team_data = TeamLeaderBoard.objects.all()
        print(all_team_data)
    
    def handle(self, *args, **options):
        self.scrape()

    