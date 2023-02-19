from datetime import datetime as dt
from datetime import timedelta as td
from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from db import base
#from ..model.game import Game

Base = declarative_base()

class Team(base):

    __tablename__ = 'team'
    id_team = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(50))
    code = Column(String(20))
    city_name = Column(String(50))
    name = Column(String(80))
    homepage = Column(String(80))
    division = Column(String(50))
    conference = Column(String(50))
    
    #player_properties_team = relationship("PlayerProperty", lazy="noload", foreign_keys="PlayerProperty.id_team", backref="property_team_player")

    #team_pred_winner = relationship("Game", lazy="noload", foreign_keys="Game.id_predic_winner", back_populates="pred_winner_team")
    #team_winner = relationship("Game", lazy="noload", foreign_keys="Game.id_winner_team", back_populates="winner_team")
    team_visitor = relationship("Game", lazy="noload", foreign_keys="Game.id_visit_team", back_populates="visit_team")
    team_home = relationship("Game", lazy="noload", foreign_keys="Game.id_home_team", back_populates="home_team")

    def __init__(self):
        pass

    def __init__(self, full_name, code, city_name, name, homepage, division, conference):
        self.full_name = full_name
        self.code = code
        self.city_name = city_name
        self.name = name
        self.homepage = homepage
        self.division = division
        self.conference = conference

    def json(self):
       return {'Need to be implemented' + 'date': self.date.strftime('%b %d %Y %I:%M%p')}