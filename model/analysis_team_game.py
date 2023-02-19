from datetime import datetime as dt
from datetime import timedelta as td
from .team import Team
from .game import Game
from .player import Player
from sqlalchemy import Column, Integer, Float, BigInteger, DateTime, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from db import base
Base = declarative_base()

class AnalysisTeamGame(base):#OK

    __tablename__ = 'analysis_team_game'
    __table_args__ = {'extend_existing': True}
    id_analysis_team = Column(Integer, primary_key=True, autoincrement=True)
    id_team = Column(Integer, ForeignKey('team.id_team'))
    id_game = Column(Integer, ForeignKey('game.id_game'))
    
    #REvisar
    

    team_of_stats = relationship("Team", lazy="noload", foreign_keys="AnalysisTeamGame.id_team")#, backref="team_stats")
    game_of_stats = relationship("Game", lazy="noload", foreign_keys="AnalysisTeamGame.id_game")#, backref="game_stats")

    def __init__(self):
        pass

    def __init__(self, team_id, game_id):
        self.id_team = team_id
        self.id_game = game_id

    def json(self):
       return {'Need to be implemented' + 'date': self.date.strftime('%b %d %Y %I:%M%p')}\
