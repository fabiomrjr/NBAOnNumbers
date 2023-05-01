from datetime import datetime as dt
from datetime import timedelta as td
from .team import Team
from .game import Game
from .player import Player
from sqlalchemy import Column, Integer, Float, BigInteger, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from resources.db import base
#Base = declarative_base()

class AnalysisPlayerGame(base):#OK

    __tablename__ = 'analysis_player_game'
    __table_args__ = {'extend_existing': True}
    id_player_game_statistic = Column(Integer, primary_key=True, autoincrement=True)
    id_player = Column(Integer, ForeignKey('player.id_player'))
    id_team = Column(Integer, ForeignKey('team.id_team'))
    id_game = Column(Integer, ForeignKey('game.id_game'))
    pts_media = Column(Integer)

    player = relationship("Player", lazy="noload", foreign_keys="AnalysisPlayerGame.id_player")#, backref="player_stats")
    game = relationship("Game", lazy="noload", foreign_keys="AnalysisPlayerGame.id_game")#, backref="game_stats")
    team = relationship("Team", lazy="noload", foreign_keys="AnalysisPlayerGame.id_team")#, backref="team_player_stats")

    def __init__(self, team_id, game_id, player_id, pts_media):
        self.id_team = team_id
        self.id_game = game_id
        self.id_player = player_id
        self.pts_media = pts_media

    def json(self):
       return {'Need to be implemented' + 'date': self.date.strftime('%b %d %Y %I:%M%p')}\
