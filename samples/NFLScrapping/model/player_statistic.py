from datetime import datetime as dt
from datetime import timedelta as td
from ..model.team import Team
from ..model.game import Game
from ..model.player import Player
from sqlalchemy import Column, Integer, Float, BigInteger, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from db import base
Base = declarative_base()

class PlayerStatistic(base):

    __tablename__ = 'player_game_statistic'
    __table_args__ = {'extend_existing': True}
    id_player_game_statistic = Column(Integer, primary_key=True, autoincrement=True)
    id_player = Column(Integer, ForeignKey('player.id_player'))
    id_team = Column(Integer, ForeignKey('team.id_team'))
    id_game = Column(Integer, ForeignKey('game.id_game'))
    passing_compl = Column(Integer)
    passing_att = Column(Integer)
    passing_yds = Column(Integer)
    passing_td = Column(Integer)
    passing_int = Column(Integer)
    passing_sacks = Column(Integer)
    passing_yds_lost = Column(Integer)
    passing_longest_compl = Column(Integer)
    rate = Column(Float(precision=2))
    rushing_att = Column(Integer)
    rushing_yds = Column(Integer)
    rushing_td = Column(Integer)
    rushing_longest = Column(Integer)
    receiving_target = Column(Integer)
    receiving_receptions = Column(Integer)
    receiving_yds = Column(Integer)
    receiving_td = Column(Integer)
    receiving_longest = Column(Integer)
    fumbles = Column(Integer)
    fumbles_lost = Column(Integer)

    player = relationship("Player", lazy="noload", foreign_keys="PlayerGameStatistic.id_player")#, backref="player_stats")
    team = relationship("Team", lazy="noload", foreign_keys="PlayerGameStatistic.id_team")#, backref="team_player_stats")

    def __init__(self):
        pass

    def json(self):
       return {'Need to be implemented' + 'date': self.date.strftime('%b %d %Y %I:%M%p')}\
