import numpy as np
import pandas as pd

from sqlalchemy import create_engine, text, and_, update
from sqlalchemy.orm import sessionmaker, subqueryload, selectinload
from datetime import datetime as dt

from source.dao.team_dao import TeamDAO
from source.dao.game_dao import GameDAO
from resources.util import util

from source.scrapers.hockey_reference.br_nhl_league_scrap import HockeyReferenceLeagueScheduleScrap

class NHLGamesDBCreatorService():
    def __init__(self):
        pass
        #DAO.__init__(self)

    def createNHLGames(self):
        startDate = dt.now()
        
        urls = [
            #'leagues/NBA_2023_games-october.html',
            'leagues/NHL_2023_games.html'
            ]

        for url in urls:
            print('-------------------------')
            print('Consultando ' + url)
            scheduledf = HockeyReferenceLeagueScheduleScrap().checkAllSchedule(url)
            print('Fim da Consulta')
            print('Criando Jogos na base de dados')
            self.createNHLGamesByScheduleDF(scheduledf)
            print('Fim da criação de Jogos na base de dados')
        
        endDate = dt.now()
        print("Jogos NHL atualizados em seconds " + str((endDate - startDate).total_seconds()))
    
    def createNHLGamesByScheduleDF(self, scheduleDF):
    
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