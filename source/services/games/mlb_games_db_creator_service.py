import numpy as np
import pandas as pd
import resources.config as config

from sqlalchemy import create_engine, text, and_, update
from sqlalchemy.orm import sessionmaker, subqueryload, selectinload

from source.dao.team_dao import TeamDAO
from source.dao.game_dao import GameDAO
from resources.util import util

from source.scrapers.baseball_reference.br_mlb_league_scrap  import BaseballReferenceLeagueScheduleScrap
from source.scrapers.mlb_web_site.mlb_web_site_scrap  import MlbLeagueScheduleScrap

class MLBGamesDBCreatorService():
    def __init__(self):
        pass
        #DAO.__init__(self)

    def createMLBGames(self):
        urls = [
            #'leagues/majors/2022-schedule.shtml',
            #'leagues/majors/2023-schedule.shtml'
            '/scores/2023-04-03'
            ]

        for url in urls:
            print('-------------------------')
            print('Consultando ' + url)
            #scheduledf = BaseballReferenceLeagueScheduleScrap().checkAllSchedule(url)
            scheduledf = MlbLeagueScheduleScrap().checkAllSchedule(url)
            print('Fim da Consulta')
            print('Criando Jogos na base de dados')
            #self.createMLBGamesByScheduleDF(scheduledf)
            print('Fim da criação de Jogos na base de dados')
    
    def createMLBGamesByScheduleDF(self, scheduleDF):
    
        listGames = []
        for index, row in scheduleDF.iterrows():
            teamVisitorObject = TeamDAO().getTeamByFullName(row['Visitor'])
            teamHomeObject = TeamDAO().getTeamByFullName(row['Home'])
            
            visitorPTS = util().emptyOrNan(row['G'])
            homePTS = util().emptyOrNan(row['G.1'])
            attend = util().emptyOrNan(row['Att.'])
                
            boxScore = "" if row['BoxScoreLink'] != row['BoxScoreLink'] else row['BoxScoreLink']
            arena = ""
            overtime_type = row['Overtime']
            Overtime = True if row['Overtime'] != "" else False
            
            gameSaved = GameDAO().createOrUpdateGame(teamHomeObject.id_team, teamVisitorObject.id_team, 
                                                 row['DateTime'], homePTS, visitorPTS, boxScore, 
                                                 Overtime, attend, arena, overtime_type, "NHL")
            listGames.append(gameSaved)
        
        return listGames