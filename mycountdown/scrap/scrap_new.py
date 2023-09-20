from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os
from datetime import datetime


# Initialize the WebDriver (You might need to specify the path to your webdriver executable)
driver = webdriver.Chrome()

# Open a web page with an iframe
driver.get("https://www.formula1.com/en/results.html/2023/drivers.html")

try:
    # Wait for the iframe to appear (change the locator to match your specific iframe)
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//iframe[@title='SP Consent Message']"))
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
    
    wait = WebDriverWait(driver, 10)
    table = wait.until(EC.presence_of_element_located((By.XPATH, "//table[@class='resultsarchive-table']")))
    #print(table.get_attribute('innerHTML'))
    rows = table.find_elements(By.XPATH, ".//tr")
    
    data_list = []

# Loop through each row and extract the text or perform other actions as needed
    for row in rows:
    # Extract the text from the row or perform other actions here
        row_text = row.text
        row_text_split = row_text.split(' ')
        pos = row_text_split[0]
        name = row_text_split[1]+' '+row_text_split[2]
        point = row_text_split[-1]

        row_data = {
        "pos": pos,
        "name": name,
        "point": point
    }
        data_list.append(row_data)

    if data_list:
        data_list = data_list[1:]
    json_data = json.dumps(data_list)

# You can print the JSON data or save it to a file
    print(json_data)
    
    # Print the text of each row
        #print(pos,name,point)
    file_directory = os.getcwd()+'/static/scrap/'
    file_path = file_directory+'drivers.json'

# Write the dictionary to a JSON file
    with open(file_path, "w") as json_file:
        json.dump(data_list, json_file)
    




except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the WebDriver
    driver.quit()
