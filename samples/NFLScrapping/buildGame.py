import pandas as pd
import requests
import re
from urllib.request import urlopen
from .builder.game_builder import GameBuilder
from bs4 import BeautifulSoup, Comment

class BuildGame:
    def __init__(self):
     pass

    def check(self, url):

        req = requests.get(url)
        if req.status_code == 200:
            print('Requisição bem sucedida!')
            content = req.content

        #table = soup.find_all(name='table')
        #res = urlopen(req)
        #rawpage = req.read().decode("utf-8")
        #page = rawpage.replace("<!-->", "")
        soupDefault = BeautifulSoup(content, 'html.parser')

        comments = soupDefault.findAll(text=lambda text:isinstance(text, Comment))
        [comment.extract() for comment in comments]

        soupComments = BeautifulSoup(str(comments), 'html.parser')

        table_game_info = soupDefault.find_all('div', attrs={'class':'scorebox_meta'})
        table_plyer_offense = soupDefault.find_all('div', attrs={'id':'div_player_offense'})
        table_plyer_difense = soupComments.find_all('div', attrs={'id':'div_player_defense'})
        table_team_stats = soupComments.find_all('table', attrs={'id':'team_stats'})
        table_scorebox = soupDefault.find_all('div', attrs={'class': 'scorebox'})

        table_str = str(table_game_info[0])
        soupGameInfo = BeautifulSoup(table_str, 'html.parser')
        resultTest = str(soupGameInfo.findChildren("div" , recursive=False)[0].text)

        table_str = str(table_scorebox[0])
        soupScoreBox = BeautifulSoup(table_str, 'html.parser')
        children_scoreBox = str(soupScoreBox.findChildren("div", recursive=False)[0].text)
        scoreBoxSplitted = children_scoreBox.split("\n")

        dayGame = resultTest[0:resultTest.find("Start Time")]
        startTime = resultTest[resultTest.find("Start Time:") + len("Start Time:"): resultTest.find("Stadium")]
        #Stadium = resultTest[resultTest.find("Stadium:") + len("Stadium:"): resultTest.find("Attendance")]
        coach_home = scoreBoxSplitted[18]
        score_home = scoreBoxSplitted[13]
        coach_visit = scoreBoxSplitted[37]
        score_visit = scoreBoxSplitted[32]
        home_name = scoreBoxSplitted[9]
        visit_name = scoreBoxSplitted[28]

        #table_test = soupDefault.find_all('div', attrs={'class': 'scorebox'})
        table_player_offense_df = pd.read_html(str(table_plyer_offense[0]))[0]
        table_player_defense_df = pd.read_html(str(table_plyer_difense[0]))[0]
        table_team_stats_df = pd.read_html(str(table_team_stats[0]))[0]
        #table_scorebox_df = pd.read_html(str(table_scorebox[0]))[0]

        GameBuilder().createGame(dayGame, startTime, table_team_stats_df, coach_home, coach_visit, score_home, score_visit, table_player_offense_df, table_player_defense_df)
        #index = pd.date_range('1/1/2000', periods=8)
        #s = pd.Series(np.random.randn(5), index=[ 'a', 'b', 'c', 'd', 'e' ])
        #df = pd.DataFrame(np.random.randn(8, 3), index=index, columns=[ 'A', 'B', 'C' ])
        #print("A")

