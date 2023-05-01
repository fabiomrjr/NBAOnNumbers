import requests
import re
import numpy as np
import pandas as pd
import resources.config as config
from resources.util import util

from bs4 import BeautifulSoup, Comment

class HockeyReferenceLeagueScheduleScrap:
    def __init__(self):
     pass

    def checkAllSchedule(self, url):
        #dtFinal = pd.DataFrame()
        
        pageBS = self.callPage(config.nhlBaseURL + url)
        df1 = self.extractTable(pageBS)
        #dtFinal = dtFinal.append(df1)
            
        return df1
    
    def callPage(self, url):
        req = requests.get(url)
        content = ''
        if req.status_code == 200:
            print('Requisição bem sucedida! Week ')
            content = req.content

        pageBS = BeautifulSoup(content, 'html.parser')
        return pageBS
    
    def extractTable(self, pageBS):
        scheduleTable = pageBS.find_all('table', attrs={'id':'games'})
        scheduleStringTable = str(scheduleTable)
        scheduleTableBS = BeautifulSoup(scheduleStringTable, 'html.parser')
        
        dfbase=pd.DataFrame()
        dfbase=pd.read_html(str(scheduleTableBS))[0]
        
        dfbase = dfbase.drop(columns=['Notes', 'LOG'])
        
        bodySchedule = scheduleTableBS.find_all('tbody')
        bodyStringSchedule = str(bodySchedule)
        
        bodyScheduleBS = BeautifulSoup(bodyStringSchedule, 'html.parser')
        lineTableData = bodyScheduleBS.find_all('th')
        #lineStringTableData = str(lineTableData)
        #lineTableDataBS = BeautifulSoup(lineStringTableData, 'html.parser')

        #lineDataTable = lineTableDataBS.find_all('td')

        dataBoxScoreLink = []
        
        for lineData in lineTableData:
            lineDataBS = BeautifulSoup(str(lineData.extract()), 'html.parser')
            value = lineDataBS.get_text()
            
            if re.search('date_game', str(lineDataBS)) != None:
                result = re.search('a href="(.*)"', str(lineDataBS))
                if result == None:
                    dataBoxScoreLink.append("")
                else:    
                    dataBoxScoreLink.append(result.group(1))
                    
        data = {
            "BoxScoreLink": dataBoxScoreLink
            }
        
        dfbase = dfbase.assign(BoxScoreLink=dataBoxScoreLink)
        #dfbase = dfbase.assign(Overtime=dataOvertime)
        
        dates = []
        utilnew = util()
        for index, row in dfbase.iterrows():
            dates.append(utilnew.getDateTimeByDayAndTime(row['Date'], None, "nhl"))
            
        dfbase = dfbase.assign(DateTime=dates)
        
        dfbase.rename(columns={'Unnamed: 5': 'Overtime'}, inplace=True)
        dfbase = dfbase.fillna('')
        
        return dfbase