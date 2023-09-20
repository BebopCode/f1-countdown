from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime
from pytz import timezone
import pytz
import json
from django.contrib.staticfiles import finders

json_file_path = 'drivers.json'
if json_file_path:
    with open(json_file_path, 'r') as json_file:
        drivers = json.load(json_file)

    # Now 'drivers' should be a list of dictionaries

print(type(drivers))