import requests
import re
import numpy as np
import pandas as pd

from selenium import webdriver
from datetime import datetime as dt
from bs4 import BeautifulSoup, Comment
from requests_html import HTMLSession
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BetanoScrap():
    def __init__(self):
        pass
        #DAO.__init__(self)
    
    def getNHLOddsDF(self):
        
        url = "https://br.betano.com/sport/hoquei-no-gelo/ligas/10118r/"
        a = ""
        driver = webdriver.Chrome()
        driver.implicitly_wait(20) # seconds
        driver.get(url)
        try:
            element = driver.find_element(By.CLASS_NAME, "toggle-switch__slider")
            driver.execute_script("arguments[0].click();", element)
            a = driver.find_elements(By.CLASS_NAME, "events-list__grid")[0].get_attribute("outerHTML")
        finally:
            driver.quit()
            
        return pd.read_html(str(a))[0]
    
    def getNBAOddsDF(self):
        
        url = "https://br.betano.com/sport/basquete/eua/nba/17106/"
        a = ""
        element = ""
        driver = webdriver.Chrome()
        driver.implicitly_wait(15) # seconds
        driver.get(url)
        try:
            element = driver.find_element(By.CLASS_NAME, "toggle-switch__slider")
            driver.execute_script("arguments[0].click();", element)
            a = driver.find_elements(By.CLASS_NAME, "events-list__grid__event")[0].get_attribute("outerHTML")
        finally:
            driver.quit()
            
        return pd.read_html(str(a))[0]