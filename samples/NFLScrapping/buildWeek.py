import pandas as pd
import requests
import re
import numpy as np
from .builder.team_builder import TeamBuilder
from bs4 import BeautifulSoup, Comment

base_url = 'https://www.pro-football-reference.com'

class BuildWeek:
    def __init__(self):
     pass

    def check(self, url, start, end):
        x = []

        #TeamBuilder().createDefaultTeams()

        for i in range(start, end):
            string1 = url + '/week_' + str(i) + '.htm'
            req = requests.get(string1)
            content = ''
            if req.status_code == 200:
                print('Requisição bem sucedida! Week ' + str(i))
                content = req.content

            soup = BeautifulSoup(content, 'html.parser')

            table = soup.find_all('table', attrs={'class':'teams'})
            strTable = str(table)

            soup3 = BeautifulSoup(strTable, 'html.parser')
            table1 = soup3.find_all('td', attrs={'class':'right gamelink'})

            for item in table1:
                result = re.search('a href="(.*)"', str(item))
                x.append(base_url + result.group(1))

        print(x)
        return x