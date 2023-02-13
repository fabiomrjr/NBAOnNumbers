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

def checkAllSchedule():
    dtFinal = pd.DataFrame()
    #for month in x:
    pageBS = callPage("https://www.nba.com/game/det-vs-cle-0022200822/box-score")
    #pageBS = callPage("https://www.nba.com/games?date=2023-02-21") # no games
    #pageBS = callPage("https://www.nba.com/games?date=2023-02-24) # agendados
    
    df1 = extractTable(pageBS)
    dtFinal = dtFinal.append(df1)
    #print(df1)
    return dtFinal

def callPage(url):
    b = ""
    element = ""
    driver = webdriver.Chrome()# ChromeOptions()# PhantomJS()
    #driver = webdriver.Firefox()
    driver.implicitly_wait(10) # seconds
    driver.get(url)
    #try:
    #    element = WebDriverWait(driver, 15).until(
    #        EC.presence_of_element_located((By.CLASS_NAME, "StatsTableBody_tbody__uvj_P"))
    #    )
    #    b=(element.text)
    #finally:
    #    driver.quit()
    
    a = (driver.find_elements(By.CLASS_NAME, "StatsTableBody_tbody__uvj_P"))[0].get_attribute("outerHTML")
    g = driver.find_elements(By.CLASS_NAME, "GameBoxscoreInactivePlayers_label__9GQfI")
    p = driver.find_elements(By.CLASS_NAME, "GameBoxscoreInactivePlayers_player__sop6b")
    t = driver.find_elements(By.CLASS_NAME, "GameBoxscoreTablePlayer_gbp__mPF20")
    
    #print(a)
    #html = driver.page_source
    #driver.quit()
    #tt= BeautifulSoup(html, 'html.parser')
    
    for item in g:
        print(item.text)
    print("---------------------")
    for item in p:
            print(item.text)
    print("---------------------")
    print(a[0].text)
    print("---------------------")
    print(a[1].text)
    print("---------------------")
    driver.quit()
    
    
    
    req = requests.get(url)
    content = ''
    if req.status_code == 200:
        print('Requisição bem sucedida! Day at NBA !')
        content = req.content

    pageBS = BeautifulSoup(content, 'html.parser')
    return pageBS

def extractTable(pageBS):
    
    boxScoreTable = str(pageBS.find_all('tbody', attrs={'class':'StatsTableBody_tbody__uvj_P'}))
    df = pd.read_html(boxScoreTable)
    print(df)
    #for item in boxScoreTable:
    #    lineDataBS = BeautifulSoup(str(item.extract()), 'html.parser')
    #    value = lineDataBS.get_text()
    #    if value == "BOX SCORE":
    #        result = re.search('href="(.*)"', str(lineDataBS))
    #        print(result.group(1))

startDate = dt.now()
df = checkAllSchedule()
#gamedf = NBAScheduleScrap().checkAllSchedule()
#leagueScheduledf = BasketballReferenceLeagueScheduleScrap().checkAllSchedule()

##for link in leagueScheduledf.get('BoxScoreLink'):
##    gamedf = GameScrap().check(link)
#gamedf = BasketballReferenceGameScrap().check("/boxscores/202210180GSW.html")

endDate = dt.now()
print("Finish Game Builder. Seconds " + str((endDate - startDate).total_seconds()))

 #teamjogador <table class="StatsTable_table__Ejk5X"><thead class="StatsTableHead_thead__omZuF"><tr><th>PLAYER</th><th 