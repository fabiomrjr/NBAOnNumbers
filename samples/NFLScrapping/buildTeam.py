import pandas as pd
import requests
from bs4 import BeautifulSoup, Comment
from datetime import datetime as dt

from .builder.player_builder import PlayerBuilder
from .dao.team_dao import TeamDAO

baseYearArray = ["2011"]#, "2012", "2013", "2014"]

class BuildTeam:
    def __init__(self):
     pass

    def check(self):
        startDate = dt.now()
        Teams = TeamDAO().listTeamsWithHomePage()

        for baseYear in baseYearArray:
            for item in Teams:
                content = ""
                site = "https://www.pro-football-reference.com/" + item.homepage
                site = site.replace("ANOXX", str(baseYear))
                req = requests.get(site)
                if req.status_code == 200:
                    print('Requisição bem sucedida!')
                    content = req.content

                soupDefault = BeautifulSoup(content, 'html.parser')
                comments = soupDefault.findAll(text=lambda text:isinstance(text, Comment))
                [comment.extract() for comment in comments]
                soupComments = BeautifulSoup(str(comments), 'html.parser')

                table_scorebox = soupComments.find_all('div', attrs={'id':'div_games_played_team'})
                table_str = str(table_scorebox[0])

                table_roster_df = pd.read_html(table_str)[0]

                PlayerBuilder().check(table_roster_df, item, baseYear)

                print("Finish Team Builder - Base Year " + baseYear + " Team " + item.name)
            #print("Finish Team Builder - Base Year " + baseYear)
        endDate = dt.now()
        print("Finish Team Builder. Seconds " + str((endDate - startDate).total_seconds()))