import pandas as pd
import mysql.connector as connection
import pandas as pd

from sqlalchemy import create_engine, text, and_, update
from sqlalchemy.orm import sessionmaker, subqueryload, selectinload
from source.model.game import Game as game
from source.dao.dao import DAO
from source.model.player_game_statistic import PlayerGameStatistic
import resources.config as config

class GameDAO(DAO):

    def __init__(self):
        #pass
        DAO.__init__(self, config.connectionStringNBA)
        
    def createGame(home_team_id, visit_team_id, startDateTime, home_score, visit_score, gamehomepage, has_overtime, attend, arena, overtime_type, league):
        dao = DAO(config.connectionStringNBA)
        #dao.startConnection()
        
        c1 = game(home_team_id, visit_team_id, startDateTime, home_score, visit_score, gamehomepage, has_overtime, attend, arena, overtime_type, league)
        
        try:
            dao.session.add(c1)
            dao.session.commit()
        except:
            dao.session.rollback()
            raise
        
        dao.quitConnection()
        return c1

    def getGameByTeamsAndDateTime(home_team_id, visit_team_id, startDateTime):
        dao = DAO(config.connectionStringNBA)
        #dao.startConnection()
        
        try:
            item = dao.session.query(game).filter(and_(game.id_home_team == home_team_id, 
                                                       game.id_visit_team == visit_team_id, 
                                                       game.date.like("%{}%".format(startDateTime.strftime('%Y-%m-%d'))))).first()# == startDateTime.strftime('%Y-%m-%d'))).first()
        except:
            dao.session.rollback()
            raise
        dao.quitConnection()
        return item
    
    def updateGame(id_game, home_score, visit_score, gamehomepage, has_overtime, attend, arena, overtime_type, league):
        dao = DAO(config.connectionStringNBA)
        #dao.startConnection()
        
        try:
            stmt = (update(game).where(game.id_game == id_game)
                    .values(home_score = home_score, visit_score = visit_score, gamehomepage = gamehomepage, 
                            has_overtime = has_overtime, attend = attend, arena = arena, overtime_type = overtime_type, league = league))
            dao.session.execute(stmt)

            dao.session.commit()
            item = dao.session.query(game).filter(game.id_game == id_game).first()
        
        except:
            dao.session.rollback()
            raise
        dao.quitConnection()
        return item
    
    def listGamesWithoutStatistics(self):
        dao = DAO(config.connectionStringNBA)
        #dao.startConnection()
        
        try:
            
            #statement = text('select * from nbaonnumbers.game where nbaonnumbers.game.gamehomepage != "" and nbaonnumbers.game.id_game not in (select nbaonnumbers.nba_player_game_statistic.id_game from nbaonnumbers.nba_player_game_statistic);')
            #item = dao.session.execute(statement).all()
            
            #query = dao.session.query(PlayerGameStatistic).all()
            #item = dao.session.query(game).filter(and_(game.id_game.not_in(query), game.gamehomepage != "")).limit(3).all()
            item = dao.session.query(game).limit(3).all()
        except:
            dao.session.rollback()
            raise
        dao.quitConnection()
        return item
    
    def createOrUpdateGame(self, home_team_id, visit_team_id, startDateTime, home_score, visit_score, game_homepage, has_overtime, attend, arena, overtime_type, league):
        game = GameDAO.getGameByTeamsAndDateTime(home_team_id, visit_team_id, startDateTime)

        if game != None:
            return GameDAO.updateGame(game.id_game, home_score, visit_score, game_homepage, has_overtime, attend, arena, overtime_type, league)
        
        return GameDAO.createGame(home_team_id, visit_team_id, startDateTime, home_score, visit_score, game_homepage, has_overtime, attend, arena, overtime_type, league)