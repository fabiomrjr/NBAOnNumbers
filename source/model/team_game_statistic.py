from datetime import datetime as dt
from datetime import timedelta as td

from sqlalchemy import Column, Integer, Float, BigInteger, DateTime, ForeignKey, TIME, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Float, BigInteger, DateTime, ForeignKey, String
from resources.db import base
#Base = declarative_base()

class TeamGameStatistic(base):

    __tablename__ = 'team_game_statistic'
    __table_args__ = {'extend_existing': True}
    id_team_game_statistic = Column(Integer, primary_key=True, autoincrement=True)
    id_team = Column(Integer, ForeignKey('team.id_team'))
    id_game = Column(Integer, ForeignKey('game.id_game'))
    q1_score = Column(Integer)
    q2_score = Column(Integer)
    q3_score = Column(Integer)
    q4_score = Column(Integer)
    half_score = Column(Integer)
    total_score = Column(Integer)
    turnover = Column(Integer)
    min_play = Column(TIME)
    fg = Column(Integer)
    fga = Column(Integer)
    fg_perc = Column(Float(precision=3))
    three_pts = Column(Integer)
    three_pts_att = Column(Integer)
    three_pts_perc = Column(Float(precision=3))
    ft = Column(Integer)
    fta = Column(Integer)
    ft_perc = Column(Float(precision=3))
    offense_rebound = Column(Integer)
    defense_rebound = Column(Integer)
    total_rebound = Column(Integer)
    assists = Column(Integer)
    steals = Column(Integer)
    blocks = Column(Integer)
    turnovers = Column(Integer)
    personal_fouls = Column(Integer)
    pts = Column(Integer)
    plus_minos = Column(Integer)
    ts_perc = Column(Float(precision=3))
    efg_perc = Column(Float(precision=3))
    threepar_perc = Column(Float(precision=3))
    ftr_perc = Column(Float(precision=3))
    orb_perc = Column(Float(precision=3))
    drb_perc = Column(Float(precision=3))
    trb_perc = Column(Float(precision=3))
    ast_perc = Column(Float(precision=3))
    stl_perc = Column(Float(precision=3))
    blk_perc = Column(Float(precision=3))
    tov_perc = Column(Float(precision=3))
    usg_perc = Column(Float(precision=3))
    or_tg = Column(Integer)
    dr_tg = Column(Integer)
    bpm = Column(Float(precision=3))
        
    #team_of_stats
    team = relationship("Team", lazy="noload", foreign_keys="TeamGameStatistic.id_team")#, backref="team_stats")
    #game_of_stats
    game = relationship("Game", lazy="noload", foreign_keys="TeamGameStatistic.id_game")#, backref="game_stats")

    def __init__(self):
        pass

    def __init__(self, team_id, game_id, q1_score,q2_score, q3_score, q4_score, half_score, total_score, turnover, min_play, fg, fga, fg_perc, three_pts, three_pts_att, 
                 three_pts_perc, ft, fta, ft_perc, offense_rebound, defense_rebound, total_rebound, assists, steals, blocks, turnovers, personal_fouls, pts, plus_minos, 
                 ts_perc, efg_perc, threepar_perc, ftr_perc, orb_perc, drb_perc, trb_perc, ast_perc, stl_perc, blk_perc, tov_perc, usg_perc, or_tg, dr_tg, bpm):
        
        self.id_team = team_id
        self.id_game = game_id
        self.q1_score = q1_score
        self.q2_score = q2_score
        self.q3_score = q3_score
        self.q4_score = q4_score
        self.half_score = half_score
        self.total_score = total_score
        self.turnover = turnover
        self.min_play = min_play
        self.fg = fg
        self.fga = fga
        self.fg_perc = fg_perc
        self.three_pts = three_pts
        self.three_pts_att = three_pts_att
        self.three_pts_perc = three_pts_perc
        self.ft = ft
        self.fta = fta
        self.ft_perc = ft_perc
        self.offense_rebound = offense_rebound
        self.defense_rebound = defense_rebound
        self.total_rebound = total_rebound
        self.assists = assists
        self.steals = steals
        self.blocks = blocks
        self.turnovers = turnovers
        self.personal_fouls = personal_fouls
        self.pts = pts
        self.plus_minos = plus_minos
        self.ts_perc = ts_perc
        #Advanced
        self.efg_perc = efg_perc
        self.threepar_perc = threepar_perc
        self.ftr_perc = ftr_perc
        self.orb_perc = orb_perc
        self.drb_perc = drb_perc
        self.trb_perc = trb_perc
        self.ast_perc = ast_perc
        self.stl_perc = stl_perc
        self.blk_perc = blk_perc
        self.tov_perc = tov_perc
        self.usg_perc = usg_perc
        self.or_tg = or_tg
        self.dr_tg = dr_tg
        self.bpm = bpm

    def json(self):
       return {'Need to be implemented' + 'date': self.date.strftime('%b %d %Y %I:%M%p')}\
