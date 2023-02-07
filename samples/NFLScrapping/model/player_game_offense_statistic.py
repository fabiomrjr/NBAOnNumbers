from datetime import datetime as dt
from datetime import timedelta as td
from ..model.team import Team
from ..model.game import Game
from ..model.player_game_statistic import PlayerGameStatistic
from sqlalchemy import Column, Integer, Float, BigInteger, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db import base

class PlayerGameOffenseStatistic(PlayerGameStatistic):

    __tablename__ = 'player_game_offense_statistic'
    __table_args__ = {'extend_existing': True}
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

    #player = relationship("Player", lazy="joined", foreign_keys="PlayerGameStatistic.id_player")#, backref="player_stats")
    #game = relationship("Game", lazy="joined", foreign_keys="PlayerGameStatistic.id_game")#, backref="game_stats")
    #team = relationship("Team", lazy="joined", foreign_keys="PlayerGameStatistic.id_team")#, backref="team_player_stats")

    id_player_game_statistic = Column(Integer, ForeignKey('player_game_statistic.id_player_game_statistic'), primary_key=True)
    __mapper_args__ = {
        'polymorphic_identity': 'player_game_offense_statistic',
        'polymorphic_load': 'inline'
    }

    def __init__(self, team_id, game_id, player_id, passing_compl, passing_att, passing_yds, passing_td, passing_int, passing_sacks, passing_yds_lost, passing_longest_compl,
                 rate, rushing_att, rushing_yds, rushing_td, rushing_longest, receiving_target, receiving_receptions, receiving_yds, receiving_td,
                 receiving_longest, fumbles, fumbles_lost):
        super().__init__(team_id, game_id, player_id)
        self.passing_compl = passing_compl
        self.passing_att = passing_att
        self.passing_yds = passing_yds
        self.passing_td = passing_td
        self.passing_int = passing_int
        self.passing_sacks = passing_sacks
        self.passing_yds_lost = passing_yds_lost
        self.passing_longest_compl = passing_longest_compl
        self.rate = rate
        self.rushing_att = rushing_att
        self.rushing_yds = rushing_yds
        self.rushing_td = rushing_td
        self.rushing_longest = rushing_longest
        self.receiving_target = receiving_target
        self.receiving_receptions = receiving_receptions
        self.receiving_yds = receiving_yds
        self.receiving_td = receiving_td
        self.receiving_longest = receiving_longest
        self.fumbles = fumbles
        self.fumbles_lost = fumbles_lost

    def json(self):
       return {'Need to be implemented' + 'date': self.date.strftime('%b %d %Y %I:%M%p')}\
