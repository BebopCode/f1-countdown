from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os
from datetime import datetime

def time_format(input_string):
    output_datetime= datetime.strptime(input_string, "%Y-%m-%dT%H:%M:%S")
    return output_datetime.strftime("%B %d, %Y %H:%M:%S")

month = {
'01': 'JAN',
'02': 'FEB',
'03': 'MAR',
'04': 'APR',
'05': 'MAY',
'06': 'JUN',
'07': 'JUL',
'08': 'AUG',
'09': 'SEP',
'10': 'OCT',
'11': 'NOV',
'12': 'DEC'
}
# Initialize the WebDriver (You might need to specify the path to your webdriver executable)
driver = webdriver.Chrome()

# Open a web page with an iframe
driver.get("https://www.formula1.com/en/racing/2023.html")

try:
    # Wait for the iframe to appear (change the locator to match your specific iframe)
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//iframe[@id='sp_message_iframe_834700']"))
    )
    
    # Switch to the iframe
    driver.switch_to.frame(iframe)
    
    # Find and click the button inside the iframe (change the locator to match your button)
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@title='REJECT ALL']"))
    )
    button.click()
    print('button clicked')
    
    # Optionally, switch back to the default content
    driver.switch_to.default_content()
    anchor = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='hero-event']//a"))
    )
    anchor.click()
    print('anchor clicked')
    wait = WebDriverWait(driver, 10)
    h1_element = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(@class, 'race-location')]")))
    time_table = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='f1-race-hub--timetable-listings']"))
    )

    
    child_divs = time_table.find_elements(By.XPATH, "./div")

# Iterate through the child div elements and get their attributes
    month_num=child_divs[0].get_attribute("data-start-time")[5:7]
    print(month_num)
    print()
    # You can retrieve more attributes as needed
    data = {
    "Race": time_format(child_divs[0].get_attribute("data-start-time")),
    "Qualifying": time_format(child_divs[1].get_attribute("data-start-time")),
    "Practice3": time_format(child_divs[2].get_attribute("data-start-time")),
    "Practice2": time_format(child_divs[3].get_attribute("data-start-time")),
    "Practice1": time_format(child_divs[4].get_attribute("data-start-time")),
    "Country":h1_element.text,
    "Month": month[month_num]
    
    }
    print(data)

# Specify the file path where you want to save the JSON data
    file_directory = os.getcwd()+'/scrap/static/scrap/'
    file_path = file_directory+'data.json'

# Write the dictionary to a JSON file
    with open(file_path, "w") as json_file:
        json.dump(data, json_file)




except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the WebDriver
    driver.quit()
