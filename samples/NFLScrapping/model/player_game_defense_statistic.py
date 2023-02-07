from datetime import datetime as dt
from datetime import timedelta as td
from ..model.team import Team
from ..model.game import Game
from ..model.player_game_statistic import PlayerGameStatistic
from sqlalchemy import Column, Integer, Float, BigInteger, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db import base

class PlayerGameDefenseStatistic(PlayerGameStatistic):

    __tablename__ = 'player_game_defense_statistic'
    __table_args__ = {'extend_existing': True}
    defense_int = Column(Integer)
    defense_int_yds = Column(Integer)
    defense_int_tds = Column(Integer)
    defense_int_long_return = Column(Integer)
    defense_pass_def = Column(Integer)
    sacks = Column(Float(precision=2))
    tackles_comb = Column(Integer)
    tackles_solo = Column(Integer)
    tackles_ast = Column(Integer)
    tackles_for_lost = Column(Integer)
    tackles_qb_hits = Column(Integer)
    fumbles_recovery = Column(Integer)
    fumbles_yds = Column(Integer)
    fumbles_td = Column(Integer)
    fumbles_forced = Column(Integer)

    #player = relationship("Player", lazy="joined", foreign_keys="PlayerGameStatistic.id_player")#, backref="player_stats")
    #game = relationship("Game", lazy="joined", foreign_keys="PlayerGameStatistic.id_game")#, backref="game_stats")
    #team = relationship("Team", lazy="joined", foreign_keys="PlayerGameStatistic.id_team")#, backref="team_player_stats")

    id_player_game_statistic = Column(Integer, ForeignKey('player_game_statistic.id_player_game_statistic'), primary_key=True)
    __mapper_args__ = {
        'polymorphic_identity': 'player_game_defense_statistic',
        'polymorphic_load': 'inline'
    }

    def __init__(self, team_id, game_id, player_id, defense_int, defense_int_yds, defense_int_tds, defense_int_long_return,
                 defense_pass_def, sacks, tackles_comb, tackles_solo, tackles_ast, tackles_for_lost, tackles_qb_hits,
                 fumbles_recovery, fumbles_yds, fumbles_td, fumbles_forced):
        super().__init__(team_id, game_id, player_id)
        self.defense_int = defense_int
        self.defense_int_yds = defense_int_yds
        self.defense_int_tds = defense_int_tds
        self.defense_int_long_return = defense_int_long_return
        self.defense_pass_def = defense_pass_def
        self.sacks = sacks
        self.tackles_comb = tackles_comb
        self.tackles_solo = tackles_solo
        self.tackles_ast = tackles_ast
        self.tackles_for_lost = tackles_for_lost
        self.tackles_qb_hits = tackles_qb_hits
        self.fumbles_recovery = fumbles_recovery
        self.fumbles_yds = fumbles_yds
        self.fumbles_td = fumbles_td
        self.fumbles_forced = fumbles_forced

    def json(self):
       return {'Need to be implemented' + 'date': self.date.strftime('%b %d %Y %I:%M%p')}\
