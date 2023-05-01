import requests
import re
import numpy as np
import pandas as pd
import resources.config as config
from resources.util import util

from bs4 import BeautifulSoup, Comment

class MlbLeagueScheduleScrap:
    def __init__(self):
     pass

    def checkAllSchedule(self, url):
        
        pageBS = self.callPage(config.mlbWebSiteBaseURL + url)
        df1 = self.extractTable(pageBS)
            
        return df1
    
    def callPage(self, url):
        req = requests.get(url)
        content = ''
        if req.status_code == 200:
            print('Requisição bem sucedida! Game ' + url)
            content = req.content

        pageBS = BeautifulSoup(content, 'html.parser')
        return pageBS
    
    def extractTable(self, pageBS):
        tableGamesDiv = pageBS.find_all('div', attrs={'data-test-mlb':'singleGameContainer'})
        #scheduleStringTable = str(scheduleTable)
        #scheduleTableBS = BeautifulSoup(scheduleStringTable, 'html.parser')
        
        for gameDiv in tableGamesDiv:
            placar = gameDiv.find('div', attrs={'class':'TeamMatchupLayerstyle__InlineWrapper-sc-7tca6g-1 iVtGBI'}) 
            box = gameDiv.find('div', attrs={'class':'getProductButtons__ButtonWrapper-sc-bgnczd-2 dlHiDf'}) 
            print('Dados')
        
        #parentDivWithGames = pageBS.find_all('div', attrs={'class':'section_content'}) 
        #childrenDivsWithGames = parentDivWithGames[0].find_all('div')