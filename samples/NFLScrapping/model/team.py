from datetime import datetime as dt
from datetime import timedelta as td
from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from db import base
#from ..model.game import Game

Base = declarative_base()

class Team(base):

    #association_table = Table('player_property', Base.metadata,
    #                  Column('id_team', Integer, ForeignKey('team.id_team')),
    #                  Column('id_player', Integer, ForeignKey('player.id_player')))

    __tablename__ = 'team'
    id_team = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(50))
    code = Column(String(20))
    city_name = Column(String(50))
    name = Column(String(80))
    homepage = Column(String(80))
    #children = relationship("player", secondary=association_table)
    player_properties_team = relationship("PlayerProperty", lazy="noload", foreign_keys="PlayerProperty.id_team", backref="property_team_player")

    t_pred_winner = relationship("Game", lazy="noload", foreign_keys="Game.id_predic_winner", back_populates="pred_winner_team")
    t_winner = relationship("Game", lazy="noload", foreign_keys="Game.id_winner_team", back_populates="winner_team")
    t_games_as_visitor = relationship("Game", lazy="noload", foreign_keys="Game.id_visit_team", back_populates="visit_team")
    t_games_at_home = relationship("Game", lazy="noload", foreign_keys="Game.id_home_team", back_populates="home_team")

    def __init__(self):
        pass

    def __init__(self, full_name, code, city_name, name, homepage):
        self.full_name = full_name
        self.code = code
        self.city_name = city_name
        self.name = name
        self.homepage = homepage

    def json(self):
       return {'Need to be implemented' + 'date': self.date.strftime('%b %d %Y %I:%M%p')}\

