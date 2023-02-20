import requests
import re
import numpy as np
import pandas as pd
import config
from util import util

from bs4 import BeautifulSoup, Comment

class BasketballReferenceLeagueScheduleScrap:
    def __init__(self):
     pass

    def checkAllSchedule(self, url):
        dtFinal = pd.DataFrame()
        
        pageBS = self.callPage(config.baseURL + url)
        df1 = self.extractTable(pageBS)
        dtFinal = dtFinal.append(df1)
            
        return dtFinal
    
    def callPage(self, url):
        req = requests.get(url)
        content = ''
        if req.status_code == 200:
            print('Requisição bem sucedida! Week ')
            content = req.content

        pageBS = BeautifulSoup(content, 'html.parser')
        return pageBS
    
    def extractTable(self, pageBS):
        scheduleTable = pageBS.find_all('table', attrs={'id':'schedule'})
        scheduleStringTable = str(scheduleTable)
        scheduleTableBS = BeautifulSoup(scheduleStringTable, 'html.parser')
        
        dfbase=pd.DataFrame()
        dfbase=pd.read_html(str(scheduleTableBS))[0]
        dfbase = dfbase.drop(columns=['Notes', 'Unnamed: 6', 'Unnamed: 7'])
        
        bodySchedule = scheduleTableBS.find_all('tbody')
        bodyStringSchedule = str(bodySchedule)
        
        bodyScheduleBS = BeautifulSoup(bodyStringSchedule, 'html.parser')
        lineTableData = bodyScheduleBS.find_all('tr')
        lineStringTableData = str(lineTableData)
        lineTableDataBS = BeautifulSoup(lineStringTableData, 'html.parser')

        lineDataTable = lineTableDataBS.find_all('td')

        dataBoxScoreLink = []
        dataOvertime = []
        
        for lineData in lineDataTable:
            lineDataBS = BeautifulSoup(str(lineData.extract()), 'html.parser')
            value = lineDataBS.get_text()
            
            if re.search('box_score_text', str(lineDataBS)) != None:
                result = re.search('a href="(.*)"', str(lineDataBS))
                if result == None:
                    dataBoxScoreLink.append("")
                else:    
                    dataBoxScoreLink.append(result.group(1))
            elif re.search('overtimes', str(lineDataBS)) != None:
                if value == "OT":
                    dataOvertime.append(True)
                else:
                    dataOvertime.append(False)
                    
        data = {
            "BoxScoreLink": dataBoxScoreLink,
            "Overtime": dataOvertime
            }
        
        dfbase = dfbase.assign(BoxScoreLink=dataBoxScoreLink)
        dfbase = dfbase.assign(Overtime=dataOvertime)
        
        dates = []
        utilnew = util()
        for index, row in dfbase.iterrows():
            dates.append(utilnew.getDateTimeByDayAndTime(row['Date'], row['Start (ET)']))
            
        dfbase = dfbase.assign(DateTime=dates)
        return dfbase