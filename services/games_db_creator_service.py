import config
import math
import numpy as np
from sqlalchemy import create_engine, text, and_, update
from sqlalchemy.orm import sessionmaker, subqueryload, selectinload
from model.game import Game as game
from dao.team_dao import TeamDAO
from dao.game_dao import GameDAO
from dao import dao

class GamesDBCreatorService():
    def __init__(self):
        pass
        #DAO.__init__(self)
        
    def createOrUpdateGame(self, home_team_id, visit_team_id, startDateTime, home_score, visit_score, game_homepage, has_overtime, attend, arena):
        game = GameDAO.getGameByTeamsAndDateTime(home_team_id, visit_team_id, startDateTime)

        if game != None:
            return GameDAO.updateGame(game.id_game, home_score, visit_score, game_homepage, has_overtime, attend, arena)
        
        return GameDAO.createGame(home_team_id, visit_team_id, startDateTime, home_score, visit_score, game_homepage, has_overtime, attend, arena)
    
    def createGamesByScheduleDF(self, scheduleDF):
         
        listGames = []
        for index, row in scheduleDF.iterrows():
            teamVisitorObject = TeamDAO().getTeamByFullName(row['Visitor/Neutral'])
            teamHomeObject = TeamDAO().getTeamByFullName(row['Home/Neutral'])
            
            visitorPTS = 0.0 if row['PTS'] != row['PTS'] else row['PTS']
            homePTS = 0.0 if row['PTS.1'] != row['PTS.1'] else row['PTS.1']
            attend = 0.0 if math.isnan(row['Attend.']) else row['Attend.']
            boxScore = "" if row['BoxScoreLink'] != row['BoxScoreLink'] else row['BoxScoreLink']
            arena = "" if row['Arena'] != row['Arena'] else row['Arena']

            #['Date', 'Start (ET)', 'Visitor/Neutral', 'PTS', 'Home/Neutral', 'PTS.1', 'Attend.', 'Arena', 'BoxScoreLink', 'Overtime', 'DateTime']
            gameSaved = self.createOrUpdateGame(teamHomeObject.id_team, teamVisitorObject.id_team, 
                                                 row['DateTime'], homePTS, visitorPTS, boxScore, 
                                                 row['Overtime'], attend, arena)
            listGames.append(gameSaved)
        
        return listGames
    
    