import config
from sqlalchemy import create_engine, text, and_, update
from sqlalchemy.orm import sessionmaker
from model.odd import Odd
from dao.dao import DAO

class OddDAO():

    def __init__(self):
        pass
        #DAO.__init__(self)
        
    def createOdd(id_game, game_date, date, visitor_team_name, home_team_name, visitor_win_odd,
                 home_win_odd, visitor_spread, home_spread, visitor_win_spread, home_win_spread, total, total_under, total_upper):
        dao = DAO()
        dao.startConnection()
        c1 = Odd(id_game, game_date, date, visitor_team_name, home_team_name, visitor_win_odd,
                 home_win_odd, visitor_spread, home_spread, visitor_win_spread, home_win_spread, total, total_under, total_upper)

        try:
            dao.session.add(c1)
            dao.session.commit()
        except:
            dao.session.rollback()
            raise
        dao.quitConnection()
        return c1