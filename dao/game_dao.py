import config
from sqlalchemy import create_engine, text, and_, update
from sqlalchemy.orm import sessionmaker, subqueryload, selectinload
from model.game import Game as game
from dao.dao import DAO

class GameDAO():

    def __init__(self):
        pass
        #DAO.__init__(self)
        
    def createGame(home_team_id, visit_team_id, startDateTime, home_score, visit_score, gamehomepage, has_overtime, attend, arena):
        dao = DAO()
        dao.startConnection()
        
        c1 = game(home_team_id, visit_team_id, startDateTime, home_score, visit_score, gamehomepage, has_overtime, attend, arena)
        
        try:
            dao.session.add(c1)
            dao.session.commit()
        except:
            dao.session.rollback()
            raise
        
        dao.quitConnection()
        return c1

    def getGameByTeamsAndDateTime(home_team_id, visit_team_id, startDateTime):
        dao = DAO()
        dao.startConnection()
        
        try:
            item = dao.session.query(game).filter(and_(game.id_home_team == home_team_id, 
                                                       game.id_visit_team == visit_team_id, 
                                                       game.date == startDateTime.strftime("%Y-%m-%d %H:%M:00"))).first()
        except:
            dao.session.rollback()
            raise
        dao.quitConnection()
        return item
    
    def updateGame(id_game, home_score, visit_score, gamehomepage, has_overtime, attend, arena):
        dao = DAO()
        dao.startConnection()
        
        try:
            stmt = (update(game).where(game.id_game == id_game)
                    .values(home_score = home_score, visit_score = visit_score, gamehomepage = gamehomepage, 
                            has_overtime = has_overtime, attend = attend, arena = arena))
            dao.session.execute(stmt)

            dao.session.commit()
            item = dao.session.query(game).filter(game.id_game == id_game).first()
        
        except:
            dao.session.rollback()
            raise
        dao.quitConnection()
        return item