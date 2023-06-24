from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.formula1.com/en/racing/2023.html')
l = element = driver.find_element(By.CLASS_NAME, "trustarc-agree-btn")
l.click()


upcoming_race =driver.find_element(By.CLASS_NAME, "hero-event")
#print(upcoming_race.text)
upcoming_race_split = upcoming_race.text.split()
for idx, element in enumerate(upcoming_race_split):
    print(f"{element} has index{idx}\n")
    if element == 'RACE':
        race_time_index = idx +2
    


relevant_dictionary = {
    'Country':upcoming_race_split[7],
    'RaceDate':upcoming_race_split[5] [3:5],
    'Month': upcoming_race_split[6] [4:7],
    'RaceTime' : upcoming_race_split[race_time_index]
}

print(relevant_dictionary)
while(True):
    pass

