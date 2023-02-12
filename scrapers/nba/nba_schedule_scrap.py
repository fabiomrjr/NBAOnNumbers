import requests
import re
import numpy as np
import pandas as pd
import config

from bs4 import BeautifulSoup, Comment

class NBAScheduleScrap:
    def __init__(self):
     pass

    def checkAllSchedule(self):
        x = ['games?date=2023-02-06'
             ]
        dtFinal = pd.DataFrame()
        for month in x:
            pageBS = self.callPage(config.nbaBaseURL + month)
            df1 = self.extractTable(pageBS)
            dtFinal = dtFinal.append(df1)
        #print(df1)
        return dtFinal
    
    def callPage(self, url):
        req = requests.get(url)
        content = ''
        if req.status_code == 200:
            print('Requisição bem sucedida! Day at NBA !')
            content = req.content

        pageBS = BeautifulSoup(content, 'html.parser')
        return pageBS
    
    def extractTable(self, pageBS):
        
        #table = soup.find_all('table', attrs={'class':'teams'})
        scheduleTable = pageBS.find_all('a', attrs={'class':'Anchor_anchor__cSc3P TabLink_link__f_15h'})
        
        for item in scheduleTable:
            lineDataBS = BeautifulSoup(str(item.extract()), 'html.parser')
            value = lineDataBS.get_text()
            if value == "BOX SCORE":
                result = re.search('href="(.*)"', str(lineDataBS))
                print(result.group(1))
        
        #scheduleTableA = scheduleTable.find_all('a', attrs={'value':'Box Score'})
        #scheduleStringTable = str(scheduleTable)
        #scheduleTableBS = BeautifulSoup(scheduleStringTable, 'html.parser')

        #scheduleTableBS = BeautifulSoup(scheduleStringTable, 'html.parser')
        #bodySchedule = scheduleTableBS.find_all('tbody')
        #bodyStringSchedule = str(bodySchedule)
        #
        #bodyScheduleBS = BeautifulSoup(bodyStringSchedule, 'html.parser')
        #lineTableData = bodyScheduleBS.find_all('tr')
        #lineStringTableData = str(lineTableData)
        #lineTableDataBS = BeautifulSoup(lineStringTableData, 'html.parser')
#
        #lineFirstColumnTable = lineTableDataBS.find_all('th')
        #
        #lineDataTable = lineTableDataBS.find_all('td')
 #
        #dataDate = [] 
        #dataTime = [] 
        #dataVisitor = [] 
        #dataVisitorPoints = []
        #dataHome = []
        #dataHomePoints = []
        #dataBoxScoreLink =[] 
        #dataOvertime = [] 
        #dataFans = [] 
        #dataArena = []
        #
        #for lineFirstColumn in lineFirstColumnTable:
#
        #    lineFirstColumnTableBS = BeautifulSoup(str(lineFirstColumn.extract()), 'html.parser')
        #    dataDate.append(lineFirstColumnTableBS.get_text())
        #    
        #for lineData in lineDataTable:
        #    lineDataBS = BeautifulSoup(str(lineData.extract()), 'html.parser')
        #    value = lineDataBS.get_text()
        #    
        #    if re.search('game_start_time', str(lineDataBS)) != None:
        #        dataTime.append(value)
        #    elif re.search('visitor_team_name', str(lineDataBS)) != None:
        #        dataVisitor.append(value)
        #    elif re.search('visitor_pts', str(lineDataBS)) != None:
        #        dataVisitorPoints.append(value)
        #    elif re.search('home_team_name', str(lineDataBS)) != None:
        #        dataHome.append(value)
        #    elif re.search('home_pts', str(lineDataBS)) != None:
        #        dataHomePoints.append(value)
        #    elif re.search('box_score_text', str(lineDataBS)) != None:
        #        result = re.search('a href="(.*)"', str(lineDataBS))
        #        dataBoxScoreLink.append(result.group(1))
        #    elif re.search('overtimes', str(lineDataBS)) != None:
        #        if value == "OT":
        #            dataOvertime.append(True)
        #        else:
        #            dataOvertime.append(False)
        #    elif re.search('attendance', str(lineDataBS)) != None:
        #        dataFans.append(value)
        #    elif re.search('arena_name', str(lineDataBS)) != None:
        #        dataArena.append(value)
        #            
        #data = {
        #    "Date": dataDate,
        #    "Time": dataTime,
        #    "Visitor": dataVisitor,
        #    "VisitorPoints": dataVisitorPoints,
        #    "Home": dataHome,
        #    "HomePoints": dataHomePoints,
        #    "BoxScoreLink": dataBoxScoreLink,
        #    "Overtime": dataOvertime,
        #    "Fans": dataFans ,
        #    "Arena": dataArena
        #    }
        #
        #return pd.DataFrame(data)



#<a href="/game/bos-vs-det-0022200808/box-score#box-score" class="Anchor_anchor__cSc3P TabLink_link__f_15h" data-is-external="false" data-has-more="false" data-has-children="true" data-track="click" data-type="cta" data-id="nba:games:main:box-score:cta" data-text="BOX SCORE" data-content="BOS @ DET, 2023-02-06" data-content-id="0022200808" data-section="games">BOX SCORE</a>
#<li class="TabLink_tab__uKOPj"><a href="/game/bos-vs-det-0022200808/box-score#box-score" class="Anchor_anchor__cSc3P TabLink_link__f_15h" data-is-external="false" data-has-more="false" data-has-children="true" data-track="click" data-type="cta" data-id="nba:games:main:box-score:cta" data-text="BOX SCORE" data-content="BOS @ DET, 2023-02-06" data-content-id="0022200808" data-section="games">BOX SCORE</a></li>