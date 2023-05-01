import resources.config as config
import math

from sqlalchemy import create_engine, text, and_, update
from sqlalchemy.orm import sessionmaker, subqueryload, selectinload
from datetime import datetime as dt

from source.dao.team_dao import TeamDAO
from source.dao.game_dao import GameDAO

from source.scrapers.basketball_reference.br_nba_league_scrap import BasketballReferenceLeagueScheduleScrap

class NBAGamesDBCreatorService():
    def __init__(self):
        pass
        #DAO.__init__(self)
    
    def createNBAGames(self):
        startDate = dt.now()
        urls = [
            #'leagues/NBA_2023_games-october.html',
            #'/leagues/NBA_2023_games-november.html',
            #'/leagues/NBA_2023_games-december.html',
            #'/leagues/NBA_2023_games-january.html',
            #'/leagues/NBA_2023_games-february.html',
            #'/leagues/NBA_2023_games-march.html'
            '/leagues/NBA_2023_games-april.html'
            ]

        for url in urls:
            print('-------------------------')
            print('Consultando ' + url)
            scheduledf = BasketballReferenceLeagueScheduleScrap().checkAllSchedule(url)
            print('Fim da Consulta')
            print('Criando Jogos na base de dados')
            self.createNBAGamesByScheduleDF(scheduledf)
            print('Fim da criação de Jogos na base de dados')
        
        endDate = dt.now()
        print("Jogos NBA atualizados em seconds " + str((endDate - startDate).total_seconds()))
        
    def createNBAGamesByScheduleDF(self, scheduleDF):
    
        listGames = []
        for index, row in scheduleDF.iterrows():
            teamVisitorObject = TeamDAO().getTeamByFullName(row['Visitor/Neutral'])
            teamHomeObject = TeamDAO().getTeamByFullName(row['Home/Neutral'])
            
            visitorPTS = 0.0 if row['PTS'] != row['PTS'] else row['PTS']
            homePTS = 0.0 if row['PTS.1'] != row['PTS.1'] else row['PTS.1']
            attend = 0.0 if math.isnan(row['Attend.']) else row['Attend.']
            boxScore = "" if row['BoxScoreLink'] != row['BoxScoreLink'] else row['BoxScoreLink']
            arena = "" if row['Arena'] != row['Arena'] else row['Arena']
            overtime_type = 'OT' if row['Overtime'] else ''
            
            gameSaved = GameDAO().createOrUpdateGame(teamHomeObject.id_team, teamVisitorObject.id_team, 
                                                 row['DateTime'], homePTS, visitorPTS, boxScore, 
                                                 row['Overtime'], attend, arena, overtime_type, "NBA")
            listGames.append(gameSaved)
        
        return listGames