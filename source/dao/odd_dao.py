import resources.config as config
from sqlalchemy import create_engine, text, and_, update
from sqlalchemy.orm import sessionmaker
from source.model.odd import Odd
from source.dao.dao import DAO

class OddDAO():

    def __init__(self):
        pass
        #DAO.__init__(self)
        
    def createOdd(id_game, game_date, date, visitor_team_name, home_team_name, visitor_win_odd,
                 home_win_odd, visitor_spread, home_spread, visitor_win_spread, home_win_spread, total, total_under, total_upper, league):
        dao = DAO(config.connectionStringNBA)
        #dao.startConnection()
        c1 = Odd(id_game, game_date, date, visitor_team_name, home_team_name, visitor_win_odd,
                 home_win_odd, visitor_spread, home_spread, visitor_win_spread, home_win_spread, total, total_under, total_upper, league)

        try:
            dao.session.add(c1)
            dao.session.commit()
        except:
            dao.session.rollback()
            raise
        dao.quitConnection()
        return c1
    
    def updateOdd(id_odd, id_game, game_date, date, visitor_team_name, home_team_name, visitor_win_odd,
                 home_win_odd, visitor_spread, home_spread, visitor_win_spread, home_win_spread, total, total_under, total_upper, league):
        dao = DAO(config.connectionStringNBA)
        #dao.startConnection()
        
        try:
            stmt = (update(Odd).where(Odd.id_odd == id_odd)
                    .values(id_game = id_game, game_date = game_date, date = date, visitor_team_name = visitor_team_name,
                            home_team_name = home_team_name, visitor_win_odd = visitor_win_odd, home_win_odd = home_win_odd,
                            visitor_spread = visitor_spread, home_spread = home_spread, visitor_win_spread = visitor_win_spread,
                            home_win_spread = home_win_spread, total = total, total_under = total_under, total_upper = total_upper,
                            league = league))
            dao.session.execute(stmt)

            dao.session.commit()
            item = dao.session.query(Odd).filter(Odd.id_odd == id_odd).first()
        
        except:
            dao.session.rollback()
            raise
        dao.quitConnection()
        return item
    
    def listIncorrectTeamsName():
        dao = DAO(config.connectionStringNBA)
        #dao.startConnection()
        
        try:
            item = dao.session.query(Odd).filter(Odd.home_team_name == "").all()
        except:
            dao.session.rollback()
            raise
        dao.quitConnection()
        
        return item