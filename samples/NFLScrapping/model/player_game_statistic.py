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

class PlayerGameStatistic(base):

    __tablename__ = 'player_game_statistic'
    __table_args__ = {'extend_existing': True}
    id_player_game_statistic = Column(Integer, primary_key=True, autoincrement=True)
    id_player = Column(Integer, ForeignKey('player.id_player'))
    id_team = Column(Integer, ForeignKey('team.id_team'))
    id_game = Column(Integer, ForeignKey('game.id_game'))

    player = relationship("Player", lazy="noload", foreign_keys="PlayerGameStatistic.id_player")#, backref="player_stats")
    game = relationship("Game", lazy="noload", foreign_keys="PlayerGameStatistic.id_game")#, backref="game_stats")
    team = relationship("Team", lazy="noload", foreign_keys="PlayerGameStatistic.id_team")#, backref="team_player_stats")

    def __init__(self, team_id, game_id, player_id):
        self.id_team = team_id
        self.id_game = game_id
        self.id_player = player_id

    def json(self):
       return {'Need to be implemented' + 'date': self.date.strftime('%b %d %Y %I:%M%p')}\
