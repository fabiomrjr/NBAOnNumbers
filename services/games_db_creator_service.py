import config
import math
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
            
            if math.isnan(row['Attend.']):
                attend = 0.0
            else: 
                attend = row['Attend.']
            #['Date', 'Start (ET)', 'Visitor/Neutral', 'PTS', 'Home/Neutral', 'PTS.1', 'Attend.', 'Arena', 'BoxScoreLink', 'Overtime', 'DateTime']
            gameSaved = self.createOrUpdateGame(teamHomeObject.id_team, teamVisitorObject.id_team, 
                                                 row['DateTime'], row['PTS.1'], row['PTS'], row['BoxScoreLink'], 
                                                 row['Overtime'], attend, row['Arena'])
            listGames.append(gameSaved)
        
        return listGames
    
    