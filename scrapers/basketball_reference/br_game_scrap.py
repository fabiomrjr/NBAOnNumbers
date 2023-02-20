import requests
import re
import numpy as np
import pandas as pd
import config

from selenium import webdriver
from datetime import datetime as dt
from bs4 import BeautifulSoup, Comment
from requests_html import HTMLSession
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasketballReferenceGameScrap:
    def __init__(self):
     pass

    def callPage(self, url, visitCode, homeCode):
        dfbase=pd.DataFrame()
        driver = webdriver.Chrome()
        driver.implicitly_wait(10) # seconds
        driver.get(config.baseURL + url)
        try:
            visitorBasic = (driver.find_elements(By.ID, "box-" + visitCode + "-game-basic"))[0].get_attribute("outerHTML")
            visitorAdvanced = (driver.find_elements(By.ID, "box-" + visitCode + "-game-advanced"))[0].get_attribute("outerHTML")
            
            homeBasic = (driver.find_elements(By.ID, "box-" + homeCode + "-game-basic"))[0].get_attribute("outerHTML")
            homeAdvanced = (driver.find_elements(By.ID, "box-" + homeCode + "-game-advanced"))[0].get_attribute("outerHTML")
            
            incatives  = (driver.find_elements(By.XPATH, "/html/body/div[2]/div[6]/div[23]/div[1]"))
            
            dfVisitorBasic = pd.DataFrame().read_html(str(visitorBasic))[0]
            dfVisitorAdvanced = pd.DataFrame().read_html(str(visitorAdvanced))[0]
            dfHomeBasic = pd.DataFrame().read_html(str(homeBasic))[0]
            dfVisitorAdvanced = pd.DataFrame().read_html(str(homeAdvanced))[0]
            
            print("---------------------")
    
            #dfbase=dfbase.append(df,ignore_index=True)
        finally:
            driver.quit()
        
        print("---------------------")
        print(dfbase)
        print("---------------------")
        
        return dfVisitorBasic, dfVisitorAdvanced, dfHomeBasic, dfVisitorAdvanced