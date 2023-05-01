from datetime import datetime as dt
from datetime import timedelta as td

from sqlalchemy import Column, Integer, Float, BigInteger, DateTime, ForeignKey, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from resources.db import base
#Base = declarative_base()

class Game(base): #OK

    __tablename__ = 'game'
    id_game = Column(Integer, primary_key=True, autoincrement=True)
    id_visit_team = Column(Integer, ForeignKey("team.id_team"))
    id_home_team = Column(Integer, ForeignKey("team.id_team"))
    #id_winner_team = Column(Integer, ForeignKey("team.id_team"), nullable=True)
    #id_predic_winner = Column(Integer, ForeignKey("team.id_team"), nullable=True)
    home_score = Column(Integer)
    visit_score = Column(Integer)
    date = Column(DateTime)
    gamehomepage = Column(String)
    has_overtime = Column(Boolean)
    overtime_type = Column(String(3))
    attend = Column(Integer)
    arena = Column(String(50))
    league = Column(String(5))
    #
    home_team = relationship("Team", lazy="subquery", foreign_keys="Game.id_home_team")#, backref="games_at_home")
    visit_team = relationship("Team", lazy="subquery", foreign_keys="Game.id_visit_team")#, backref="games_as_visitor")
    #winner_team = relationship("Team", lazy="noload", foreign_keys="Game.id_winner_team", backref="games_winner")
    #pred_winner_team = relationship("Team", lazy="noload", foreign_keys="Game.id_predic_winner", backref="games_pred_winner")

    def __init__(self):
        pass


    def __init__(self, home_team_id, visit_team_id, startDateTime, home_score, visit_score, gamehomepage, has_overtime, attend, arena, overtime_type, league):
        self.id_visit_team = visit_team_id
        self.id_home_team = home_team_id
        self.home_score = home_score
        self.visit_score = visit_score
        self.date = startDateTime
        #self.id_winner_team = winner_team_id
        self.gamehomepage = gamehomepage
        self.has_overtime = has_overtime
        self.attend = attend
        self.arena = arena
        self.overtime_type = overtime_type
        self.league = league
    
    def json(self):
       return {'Need to be implemented' + 'date': self.date.strftime('%b %d %Y %I:%M%p')}\
