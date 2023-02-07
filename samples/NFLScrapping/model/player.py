from datetime import datetime as dt
from datetime import timedelta as td
from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from db import base
Base = declarative_base()

class Player(base):

    __tablename__ = 'player'
    id_player = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    position = Column(String(10))
    number = Column(Integer)
    active = Column(Boolean)
    status = Column(String(50))

    properties = relationship("PlayerProperty", lazy="noload", foreign_keys="PlayerProperty.id_player", backref="property_player")

    def __init__(self):
        pass

    def __init__(self, name, position, number, status, active):
        self.name = name
        self.position = position
        self.number = number
        self.active = active
        self.status = status

    def json(self):
       return {'Need to be implemented' + 'date': self.date.strftime('%b %d %Y %I:%M%p')}\
