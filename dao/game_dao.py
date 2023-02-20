import config
from sqlalchemy import create_engine, text, and_, update
from sqlalchemy.orm import sessionmaker, subqueryload, selectinload
from model.game import Game as game
from dao.dao import DAO
from model.player_game_statistic import PlayerGameStatistic

class GameDAO(DAO):

    def __init__(self):
        #pass
        DAO.__init__(self)
        
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
    
    def listGamesWithoutStatistics(self):
        dao = DAO()
        dao.startConnection()
        
        try:
            
            #statement = select(game).from_statement("select * from nbaonnumbers.game where nbaonnumbers.game.gamehomepage != '""' and nbaonnumbers.game.id_game not in (select nbaonnumbers.player_game_statistic.id_game from nbaonnumbers.player_game_statistic);")
            #item = dao.session.execute(statement) 
            #item2 = dao.session.query(game).filter(statement)
            #(PlayerGameStatistic).all()
            #item = dao.session.query(game).filter(and_(game.id_game.not_in(query), game.gamehomepage != "")).limit(3)# all()
       
            query = self.session.query(PlayerGameStatistic).all()
            item = self.session.query(game).filter(and_(game.id_game.not_in(query), game.gamehomepage != "")).limit(3).all()
        except:
            self.session.rollback()
            raise
        dao.quitConnection()
        return item