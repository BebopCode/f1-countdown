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




def show_countdown(request):
    file_path = 'data.json'
    json_file_path = finders.find('scrap/data.json')  # Replace 'yourappname' with your app's name
    if json_file_path:
        with open(json_file_path, 'r') as json_file:
            rel_dic = json.load(json_file)
   
    
    
    mycontext = {
        'Race':rel_dic["Race"],
        'Qualifying':rel_dic["Qualifying"],
        'Practice1':rel_dic["Practice1"],
        'Practice2':rel_dic["Practice2"],
        'Practice3':rel_dic["Practice3"],
        'Country':rel_dic["Country"].capitalize,
        'Month': rel_dic["Month"].capitalize
    }

    return render( request, 'scrap/countdown.html', context=mycontext )



