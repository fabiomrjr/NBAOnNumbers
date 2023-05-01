import requests
import re
import numpy as np
import pandas as pd
import resources.config as config
from resources.util import util

from bs4 import BeautifulSoup, Comment

class BaseballReferenceLeagueScheduleScrap:
    def __init__(self):
     pass

    def checkAllSchedule(self, url):
        
        pageBS = self.callPage(config.mlbBaseURL + url)
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
        count = 0
        adate = []
        avisit = []
        ahome = []
        avisit_score = []
        ahome_score = []
        aarena = []
        aattendance = []
        adataBoxScoreLink = []
        
        parentDivWithGames = pageBS.find_all('div', attrs={'class':'section_content'}) 
        childrenDivsWithGames = parentDivWithGames[0].find_all('div')
        
        for lineData in childrenDivsWithGames:
            count = count + 1
            if count >= 30: break
            
            groupChildrenDivsWithGames = lineData.find_all('p', attrs={'class':'game'})
            
            for gameData in groupChildrenDivsWithGames:
                visitor_team, home_team, visitor_score, home_score, gameLink = self.getFirstPageGameInfo(gameData)
                arena_info, attendance_info, date_info = self.getSecondPageGameInfo(gameLink)
                
            
            adate.append(date_info)
            avisit.append(visitor_team)
            ahome.append(home_team)
            avisit_score.append(visitor_score)
            ahome_score.append(home_score)
            aarena.append(arena_info)
            aattendance.append(attendance_info)
            adataBoxScoreLink.append(gameLink)

        data = {
            "date": adate,
            "visit_team": avisit,
            "home_team": ahome,
            "visit_score": avisit_score,
            "home_score": ahome_score,
            "arena": aarena,
            "attendance": aattendance,
            "game_link": adataBoxScoreLink
            }

        dfbase = pd.DataFrame().assign(data)
        
        #dfbase.rename(columns={'Unnamed: 5': 'Overtime'}, inplace=True)
        #dfbase = dfbase.fillna('')
        
        return dfbase
    
    def getFirstPageGameInfo(self, gameData):
        splited_game_info = gameData.get_text().split('\n')
        visitor_team = splited_game_info[1].strip()
        home_team = splited_game_info[4].strip()
        visitor_score = splited_game_info[2].strip().replace("(","").replace(")","").replace(" ","")
        home_score = splited_game_info[5].strip().replace("(","").replace(")","").replace(" ","")
        
        #0:
        #''
        #1:
        #' Baltimore Orioles'
        #2:
        #' (10)'
        #3:
        #' @'
        #4:
        #'  Boston Red Sox'
        #5:
        #' (9)'
        #6:
        #' \xa0\xa0\xa0\xa0Boxscore'
        #7:
        #''
        #len():
        #8
        splited_game_info_link = str(gameData).split('\n')
        gameLink = splited_game_info_link[6].split("\"")[1]
        #0:
        #'<p class="game">'
        #1:
        #'<strong> <a href="/teams/BAL/2023.shtml">Baltimore Orioles</a>'
        #2:
        #' (10)</strong>'
        #3:
        #' @'
        #4:
        #'  <a href="/teams/BOS/2023.shtml">Boston Red Sox</a>'
        #5:
        #' (9)'
        #6:
        #' \xa0\xa0\xa0\xa0<em><a href="/boxes/BOS/BOS202303300.shtml">Boxscore</a></em>'
        #7:
        #'</p>'
        #len():
        #8
        return visitor_team, home_team, visitor_score, home_score, gameLink
    
    def getSecondPageGameInfo(self, gameLink):
        if "box" in gameLink:
            game_page = self.callPage(config.mlbBaseURL + gameLink)
            game_title = game_page.find_all('div', attrs={'class':'scorebox_meta'})
            splited = str(game_title[0]).split('div')
            
            string_date = splited[2]
            string_time = splited[4]
            date_info = util().getDateTimeByDayAndTime(string_date, string_time, "mlb_boxscore")
            attendance_aux = splited[6].split(":")[1].replace(" ","").replace(",","")
            attendance_info = float(attendance_aux[0:-2])
            arena_info = splited[8].split(":")[1][1:-2]
            #00:
            #'<'
            #01:
            #' class="scorebox_meta">\n<'
            #02:
            #'>Thursday, March 30, 2023</'
            #03:
            #'><'
            #04:
            #'>Start Time: 2:10 p.m. Local</'
            #05:
            #'><'
            #06:
            #'><strong>Attendance</strong>: 36,049</'
            #07:
            #'><'
            #08:
            #'><strong>Venue</strong>: Fenway Park</'
            #09:
            #'><'
            #10:
            #'><strong>Game Duration</strong>: 3:10</'
            #11:
            #'><'
            #12:
            #'>Day Game, on grass</'
            #13:
            #'>\n<'
            #14:
            #'><em>Logos <a href="http://www.sportslogos.net/">via Sports Logos.net</a>\n            / <a href="//www.sports-reference.com/blog/2016/06/redesign-team-and-league-logos-courtesy-sportslogos-net/">About logos</a></em></'
            #15:
            #'>\n</'
            #16:
            #'>'
            #len():
            #17
        else:
            game_page = self.callPage(config.mlbBaseURL + gameLink)
            #'Baltimore Orioles vs Boston Red Sox Box Score: March 30, 2023'
            date_game_title = str(game_page.find('h1')).split(":")
            date_info = util().getDateTimeByDayAndTime(date_game_title[1], None, "mlb_preview")
            #print(game_title.get_text())
            arena_info = ""
            attendance_info = 0.0
            
        return arena_info, attendance_info, date_info