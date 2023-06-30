from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime
from pytz import timezone
import pytz

def retday():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get('https://www.formula1.com/en/racing/2023.html')
    l = element = driver.find_element(By.CLASS_NAME, "trustarc-agree-btn")
    l.click()
    upcoming_race =driver.find_element(By.CLASS_NAME, "hero-event")
    #print(upcoming_race.text)
    upcoming_race_split = upcoming_race.text.split()

    for idx, element in enumerate(upcoming_race_split):
        #print(f"{element} has index{idx}\n")
        if element == 'RACE':
            race_time_index = idx +2
    


    relevant_dictionary = {
        'Country':upcoming_race_split[7],
        'RaceDate':upcoming_race_split[5] [3:5],
        'Month': upcoming_race_split[6] [4:7],
        'RaceTime' : upcoming_race_split[race_time_index]
    }

    month ={
        'JAN':'01',
        'FEB':'02',
        'MAR':'03',
        'APR':'04',
        'MAY':'05',
        'JUN':'06',
        'JUL':'07',
        'AUG':'08',
        'SEP':'09',
        'OCT':'10',
        'NOV':'11',
        'DEC':'12',
    }


    datetime_str = f'{relevant_dictionary["RaceDate"]}/{month[relevant_dictionary["Month"]]}/23 {relevant_dictionary["RaceTime"]}:00'

    race_datetime_object = datetime.strptime(datetime_str, '%d/%m/%y %H:%M:%S')
    race_timezone={
        'Austria':'Etc/GMT+2',
        'Bahrain': 'Asia/Bahrain',
        'Saudi Arabia': 'Etc/GMT+3',
        'Australia': 'Etc/GMT+3',
        'Azerbaijan':'Etc/GMT+4',
        'Italy':'Europe/Rome',
        'Monaco':'Etc/GMT+2',
        'Spain':'Etc/GMT+2',
        'Canada':'America/Montreal',
        'Great Britain':'Etc/GMT+1',
        'Hungary':'Etc/GMT+2',
        'Belgium':'Europe/Brussels',
        'Netherlands':'Europe/Amsterdam',
        'Singapore':'Asia/Singapore',
        'Japan':'Etc/GMT+9',
        'Qatar':'Etc/GMT+3',
        'Mexico':'Etc/GMT-6',
        'Brazil':'Etc/GMT-3',
        'Abu Dhabi':'Etc/GMT+4',
    }

    flag = 1
    if flag == 1:
        race_timezone["United States"]='Etc/GMT-5'
        flag = 2
    elif flag == 2:
        race_timezone["United States"]='Etc/GMT-7'

    source_time_zone = pytz.timezone(race_timezone[relevant_dictionary["Country"]])
    print(source_time_zone)
    print(race_datetime_object)
    race_datetime_adjusted = source_time_zone.localize(race_datetime_object)
    print(race_datetime_adjusted)
    target_time_zone = pytz.timezone('Etc/UTC')
    racetime_utc= race_datetime_adjusted.astimezone(target_time_zone)
    print(racetime_utc)
    return racetime_utc
    # while(True):
    #     pass


