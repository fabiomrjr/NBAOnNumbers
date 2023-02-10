import requests
import re
import numpy as np
import pandas as pd
import config


#from .builder.team_builder import TeamBuilder
from bs4 import BeautifulSoup, Comment

class LeagueScheduleScrap:
    def __init__(self):
     pass

    def check(self):
        x = []

        #TeamBuilder().createDefaultTeams()

        #for i in range(start, end):
        string1 = config.baseURL + '/leagues/NBA_2023_games-october.html'
        req = requests.get(string1)
        content = ''
        if req.status_code == 200:
            print('Requisição bem sucedida! Week ')
            content = req.content

        soup2 = BeautifulSoup(content, 'html.parser')

        #table = soup.find_all('table', attrs={'class':'teams'})
        table = soup2.find_all('table', attrs={'id':'schedule'})
        strTable = str(table)

        soup3 = BeautifulSoup(strTable, 'html.parser')
        table1 = soup3.find_all('tbody')
        strTable2 = str(table1)
        
        soup4 = BeautifulSoup(strTable2, 'html.parser')
        table2 = soup4.find_all('tr')
        strTable3 = str(table2)

        soup7 = BeautifulSoup(strTable3, 'html.parser')
        table7 = soup7.find_all('th')
        strTable7 = str(table7)
        print(strTable7)
       # [print(comment.extract()) for comment in table7]
        for comment in table7:
            soupComments = BeautifulSoup(str(comment.extract()), 'html.parser')
            print(soupComments)
            print(soupComments.get_text())
        print("Finish String7")
        
        soup8 = BeautifulSoup(strTable3, 'html.parser')
        table8 = soup8.find_all('td')
        strTable8 = str(table8)
        print(strTable8)
        print("Finish String8")
            
        #for item in table2:
        #    print(item)
        #    
        #    soup5 = BeautifulSoup(item, 'html.parser')
        #    table3 = soup5.find_all('td')
        #    strTable4 = str(table3)
        #    for item2 in strTable4:
        #        print(item2)
            #result = re.search('a href="(.*)"', str(item))
            #x.append(base_url + result.group(1))

        #print(x)
        return