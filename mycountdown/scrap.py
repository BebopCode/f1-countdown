from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import pytz
import os 
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mycountdown.settings')
django.setup()
from scrap.models import RaceModel

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
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.binary_location = "/usr/bin/chromium-browser"

    driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
    driver.get("https://www.formula1.com/en/racing/2024.html")
    hero_div = driver.find_element(By.XPATH, '//div[@id="featuredCard"]')
    # Find the anchor tag within the hero_div
    link = hero_div.find_element(By.TAG_NAME, 'a')

# Get the href attribute
    href = link.get_attribute('href')

# Navigate to the new page
    driver.get(href)
    event_place = hero_div.find_element(By.XPATH, './/div[@class="event-place d-block"]').text
    event_title = hero_div.find_element(By.XPATH, './/div[@class="event-title f1--xxs"]').text
    event_title = event_title.title()
    print("Event Place:", event_place)
    print("Event Title:", event_title)
    driver.quit()
    driver = webdriver.Chrome() 
    driver.get(f"https://www.formula1.com/en/racing/2024/{event_place}.html")
    #driver.get(f"https://www.formula1.com/en/racing/2024/Qatar.html")
    race_div = driver.find_element(By.XPATH, './/div[contains(@class,"js-race")]')
    global gmt_offset_str
    gmt_offset_str = race_div.get_attribute('data-gmt-offset')
    race_time = convert_string_to_datetime(race_div.get_attribute('data-start-time'))
    qualifying_div = driver.find_element(By.XPATH, './/div[contains(@class,"js-qualifying")]')
    qualifying_time = convert_string_to_datetime(qualifying_div.get_attribute('data-start-time'))
    
    try:
        sprint_div = driver.find_element(By.XPATH, './/div[contains(@class,"js-sprint")]')
        sprint_time = convert_string_to_datetime(sprint_div.get_attribute('data-start-time'))
        sprint_shootout_div = driver.find_element(By.XPATH, './/div[contains(@class,"js-sprint-shootout")]')
        sprint_shootout_time = convert_string_to_datetime(sprint_shootout_div.get_attribute('data-start-time'))

    except NoSuchElementException as e:
        sprint_time = None
        sprint_shootout_time = None

    
    
    driver.quit()
    new_race_data = RaceModel(
        title = event_title,
        race = race_time,
        qualifying = qualifying_time,
        sprint = sprint_time,
        sprint_shootout = sprint_shootout_time 

    )
    new_race_data.save()

    all_race_data = RaceModel.objects.all()
    for race_data in all_race_data:
        print(race_data)
    

if __name__ =="__main__":
    scrape()

