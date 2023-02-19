import requests
import re
import numpy as np
import pandas as pd
import config
from util import util

from bs4 import BeautifulSoup, Comment
from selenium import webdriver
from datetime import datetime as dt
from bs4 import BeautifulSoup, Comment
from requests_html import HTMLSession
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NBATeamInfoScrap:
    def __init__(self):
     pass

    def getPlayers(self, url):
        
        dtFinal = pd.DataFrame()
        #pageBS = self.callPage(url)
        #df1 = self.extractTable(pageBS, url)
        df1 = self.extractTable2(url)
        if df1.empty:
            return pd.DataFrame()
        dtFinal = pd.concat([dtFinal, df1])
        return dtFinal
    
    def callPage(self, url):
        req = requests.get(url)
        content = ''
        if req.status_code == 200:
            print('Requisição bem sucedida! Week ')
            content = req.content

        pageBS = BeautifulSoup(content, 'html.parser')
        return pageBS
    
    def extractTable(self, pageBS, url):
        playersTable = pageBS.find_all('div', attrs={'class':'TeamRoster_content__Owdiz'})
        playersTableString = str(playersTable)
        playersTableBS = BeautifulSoup(playersTableString, 'html.parser')
        
        table = playersTableBS.find_all('table')
        tableString = str(table)
        tableBS = BeautifulSoup(tableString, 'html.parser')
        
        dfPlayers=pd.DataFrame()
        dfPlayers=pd.read_html(str(tableBS))[0]
        #dfbase = dfbase.drop(columns=['Notes', 'Unnamed: 6', 'Unnamed: 7'])
        
        playerlinkHtml = tableBS.find_all('a', attrs={'class':'Anchor_anchor__cSc3P'})
        playerlinkString = str(playerlinkHtml)
        playerlinkBS = BeautifulSoup(playerlinkString, 'html.parser')
    
        playerLink = []
        
        for lineData in playerlinkHtml:
            lineDataBS = BeautifulSoup(str(lineData.extract()), 'html.parser')
            value = lineDataBS.get_text()
            
            #if re.search('box_score_text', str(lineDataBS)) != None:
            result = re.search('href="(.*)"', str(lineDataBS))
            playerLink.append(result.group(1))
        
        dfPlayers = dfPlayers.assign(PlayerLink=playerLink)
        
        return dfPlayers
    
    def extractTable2(self, url):
        dfbase=pd.DataFrame()
        driver = webdriver.Chrome()
        driver.implicitly_wait(10) # seconds
        driver.get(url)
        playerLink = []
         
        try:
            dfPlayers = pd.DataFrame()
        #    element = WebDriverWait(driver, 15).until(
        #        EC.presence_of_element_located((By.CLASS_NAME, "StatsTableBody_tbody__uvj_P"))
        #    )
        #    b=(element.text)
            teamRosterRoot2 = driver.find_elements(By.CLASS_NAME, "TeamRoster_content__Owdiz")
            if len(teamRosterRoot2) == 0:
                print(url)
                return dfPlayers
            
            teamRosterRoot = teamRosterRoot2[0]
            teamRoster = (driver.find_elements(By.CLASS_NAME, "TeamRoster_content__Owdiz"))[0].get_attribute("outerHTML")
            #df=pd.read_html(str(a))[0]
            dfPlayers=pd.read_html(str(teamRoster))[0]
            
            c = teamRosterRoot.find_elements(By.XPATH, ".//a[@class='Anchor_anchor__cSc3P']")

            #a = driver.find_elements(By.CLASS_NAME, "Anchor_anchor__cSc3P")
            
            for item in c:
                subitem = item.get_attribute("outerHTML")
                lineDataBS = BeautifulSoup(str(subitem), 'html.parser')
                result = re.search('href="(.*)"', str(lineDataBS))
                
                if result != None:
                   playerLink.append(result.group(1))
            
            dfPlayers = dfPlayers.assign(PlayerLink=playerLink)
            #dfbase=dfbase.append(df,ignore_index=True)
        finally:
            driver.quit()
        
        return dfPlayers