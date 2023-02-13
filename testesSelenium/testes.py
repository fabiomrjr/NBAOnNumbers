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
#from ghost import Ghost
#from robobrowser import browser

def check():
    pageBS = callPage("https://www.basketball-reference.com/boxscores/201912010BRK.html")
    #df1 = extractTable(pageBS)
    return

def callPage(url):
    dfbase=pd.DataFrame()
    driver = webdriver.Chrome()
    driver.implicitly_wait(10) # seconds
    driver.get(url)
    try:
    #    element = WebDriverWait(driver, 15).until(
    #        EC.presence_of_element_located((By.CLASS_NAME, "StatsTableBody_tbody__uvj_P"))
    #    )
    #    b=(element.text)
        a = (driver.find_elements(By.ID, "box-MIA-game-basic"))[0].get_attribute("outerHTML")
        df=pd.read_html(str(a))[0]
        dfbase=dfbase.append(df,ignore_index=True)
    finally:
        driver.quit()
    
    print("---------------------")
    print(dfbase)
    print("---------------------")
    driver.quit()
    
    return dfbase
    
startDate = dt.now()
df = check()
#gamedf = NBAScheduleScrap().checkAllSchedule()
#leagueScheduledf = BasketballReferenceLeagueScheduleScrap().checkAllSchedule()

##for link in leagueScheduledf.get('BoxScoreLink'):
##    gamedf = GameScrap().check(link)
#gamedf = BasketballReferenceGameScrap().check("/boxscores/202210180GSW.html")

endDate = dt.now()
print("Finish Game Builder. Seconds " + str((endDate - startDate).total_seconds()))