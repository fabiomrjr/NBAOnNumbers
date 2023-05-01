from datetime import datetime as dt
from datetime import timedelta as td
from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from resources.db import base
#Base = declarative_base()

class Player(base):#OK

    __tablename__ = 'player'
    id_player = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    position = Column(String(10))
    number = Column(Integer)
    player_link = Column(String(60))
    birth = Column(DateTime)

    #properties = relationship("PlayerProperty", lazy="noload", foreign_keys="PlayerProperty.id_player", backref="property_player")

    def __init__(self):
        pass

    def __init__(self, name, position, number, player_nba_link):
        self.name = name
        self.position = position
        self.number = number
        self.player_nba_link = player_nba_link

    def json(self):
       return {'Need to be implemented' + 'date': self.date.strftime('%b %d %Y %I:%M%p')}