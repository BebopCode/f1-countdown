from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime
from pytz import timezone


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

now_utc = datetime.now(timezone('UTC'))
print(now_utc)


print(race_datetime_object.tzinfo)
print(now_utc.tzinfo)
#race_datetime_object = race_datetime_object
while(True):
    pass

