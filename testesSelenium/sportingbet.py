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
    pageBS = callPage("https://www.betika.com/en-ke/s/basketball/usa-nba")
    #df1 = extractTable(pageBS)
    return

def callPage(url):
    
    b = ""
    element = ""
    driver = webdriver.Chrome()# ChromeOptions()# PhantomJS()
    #driver = webdriver.Firefox()
    driver.implicitly_wait(15) # seconds
    driver.get(url)
    #try:
    #    element = WebDriverWait(driver, 15).until(
    #        EC.presence_of_element_located((By.CLASS_NAME, "StatsTableBody_tbody__uvj_P"))
    #    )
    #    b=(element.text)
    #finally:
    #    driver.quit()
    
    a = driver.find_elements(By.CLASS_NAME, "prebet-match__teams")
    b = driver.find_elements(By.CLASS_NAME, "prebet-match__odds__container")
    #b = driver.find_elements(By.CLASS_NAME, "grid-six-pack-wrapper ng-star-inserted")
    
    print("---------------------")
    print(a[0].text)
    print("---------------------")
    print(b[0].text)
    print("---------------------")
    driver.quit()
    
    #print(html)
    #soup = BeautifulSoup(html, 'lxml')
    #req = browser.get(url) #requests.get(url)
    #teste = requests()
    #teste.html.render(sleep=5, keep_page=True)
    req = requests.get("https://www.basketball-reference.com/boxscores/201912010BRK.html", time.sleep(10))
    content = ''
    if req.status_code == 200:
        print('Requisição bem sucedida! Game ')
        content = req.content

    #html = browser.page_source
    return BeautifulSoup(content, 'html.parser')
    
startDate = dt.now()
df = check()
#gamedf = NBAScheduleScrap().checkAllSchedule()
#leagueScheduledf = BasketballReferenceLeagueScheduleScrap().checkAllSchedule()

##for link in leagueScheduledf.get('BoxScoreLink'):
##    gamedf = GameScrap().check(link)
#gamedf = BasketballReferenceGameScrap().check("/boxscores/202210180GSW.html")

endDate = dt.now()
print("Finish Game Builder. Seconds " + str((endDate - startDate).total_seconds()))