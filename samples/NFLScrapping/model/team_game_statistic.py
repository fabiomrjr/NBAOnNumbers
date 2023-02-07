from datetime import datetime as dt
from datetime import timedelta as td
from ..model.team import Team
from ..model.game import Game
from ..model.player import Player
from sqlalchemy import Column, Integer, Float, BigInteger, DateTime, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from db import base
Base = declarative_base()

class TeamGameStatistic(base):

    __tablename__ = 'team_game_statistic'
    __table_args__ = {'extend_existing': True}
    id_team_statistic = Column(Integer, primary_key=True, autoincrement=True)
    id_team = Column(Integer, ForeignKey('team.id_team'))
    id_game = Column(Integer, ForeignKey('game.id_game'))
    first_downs = Column(Integer)
    rush_att = Column(Integer)
    rush_yds = Column(Integer)
    rush_yds_tds = Column(Integer)
    passing_compl = Column(Integer)
    passing_att = Column(Integer)
    passing_yds = Column(Integer)
    passing_td = Column(Integer)
    passing_int = Column(Integer)
    passing_sacks = Column(Integer)
    passing_yds_lost = Column(Integer)
    net_pass_yards = Column(Integer)
    total_yards = Column(Integer)
    fumbles = Column(Integer)
    fumbles_lost = Column(Integer)
    turnovers = Column(Integer)
    penalties = Column(Integer)
    penalties_yards = Column(Integer)
    third_down = Column(Integer)
    third_down_convertion = Column(Integer)
    fourth_down = Column(Integer)
    fourth_down_convertion = Column(Integer)
    time_of_possession_min = Column(Float(precision=2))

    team_of_stats = relationship("Team", lazy="noload", foreign_keys="TeamGameStatistic.id_team")#, backref="team_stats")
    game_of_stats = relationship("Game", lazy="noload", foreign_keys="TeamGameStatistic.id_game")#, backref="game_stats")

    def __init__(self):
        pass

    def __init__(self, team_id, game_id, first_downs, rush_att, rush_yds, rush_yds_tds, passing_compl, passing_att, passing_yds, passing_td,
                 passing_int, passing_sacks, passing_yds_lost, net_pass_yards, total_yards, fumbles, fumbles_lost, turnovers, penalties,
                 penalties_yards, third_down, third_down_convertion, fourth_down, fourth_down_convertion, time_of_possession_min):
        self.id_team = team_id
        self.id_game = game_id
        self.first_downs = first_downs
        self.rush_att = rush_att
        self.rush_yds = rush_yds
        self.rush_yds_tds = rush_yds_tds
        self.passing_compl = passing_compl
        self.passing_att = passing_att
        self.passing_yds = passing_yds
        self.passing_td = passing_td
        self.passing_int = passing_int
        self.passing_sacks = passing_sacks
        self.passing_yds_lost = passing_yds_lost
        self.net_pass_yards = net_pass_yards
        self.total_yards = total_yards
        self.fumbles = fumbles
        self.fumbles_lost = fumbles_lost
        self.turnovers = turnovers
        self.penalties = penalties
        self.penalties_yards = penalties_yards
        self.third_down = third_down
        self.third_down_convertion = third_down_convertion
        self.fourth_down = fourth_down
        self.fourth_down_convertion = fourth_down_convertion
        self.time_of_possession_min = time_of_possession_min

    def json(self):
       return {'Need to be implemented' + 'date': self.date.strftime('%b %d %Y %I:%M%p')}\
