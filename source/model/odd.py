from datetime import datetime as dt
from datetime import timedelta as td
from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from resources.db import base
#Base = declarative_base()

class Odd(base):#OK

    __tablename__ = 'odds'
    id_odd = Column(Integer, primary_key=True, autoincrement=True)
    id_game = Column(Integer)
    game_date = Column(DateTime)
    date = Column(DateTime)
    league = Column(String(5))
    visitor_team_name = Column(String(80))
    home_team_name = Column(String(80))
    visitor_win_odd = Column(Float(precision=2))
    home_win_odd = Column(Float(precision=2))
    visitor_spread = Column(Float(precision=2))
    home_spread = Column(Float(precision=2))
    visitor_win_spread = Column(Float(precision=2))
    home_win_spread = Column(Float(precision=2))
    total = Column(Float(precision=2))
    total_under = Column(Float(precision=2))
    total_upper = Column(Float(precision=2))

    def __init__(self):
        pass

    def __init__(self, id_game,game_date, date, visitor_team_name, home_team_name, visitor_win_odd,
                 home_win_odd, visitor_spread, home_spread, visitor_win_spread, home_win_spread, total, total_under, total_upper, league):
        self.id_game = id_game
        self.game_date = game_date
        self.date = date
        self.visitor_team_name = visitor_team_name
        self.home_team_name = home_team_name
        self.visitor_win_odd = visitor_win_odd
        self.home_win_odd = home_win_odd
        self.visitor_spread = visitor_spread
        self.home_spread = home_spread
        self.visitor_win_spread = visitor_win_spread
        self.home_win_spread = home_win_spread
        self.total = total
        self.total_under = total_under
        self.total_upper = total_upper
        self.league = league

    def json(self):
       return {'Need to be implemented' + 'date': self.date.strftime('%b %d %Y %I:%M%p')}