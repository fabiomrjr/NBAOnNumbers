from datetime import datetime as dt
from datetime import timedelta as td
from sqlalchemy import Column, Integer, Float, BigInteger, DateTime, ForeignKey, TIME, Boolean
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
    #Revisar
    
    min_play = Column(TIME)
    fg = Column(Integer)
    fga = Column(Integer)
    fg_perc = Column(Integer)
    three_pts = Column(Integer)
    three_pts_att = Column(Integer)
    three_pts_perc = Column(Integer)
    ft = Column(Integer)
    fta = Column(Integer)
    ft_perc = Column(Integer)
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
    active = Column(Boolean)

    player = relationship("Player", lazy="noload", foreign_keys="PlayerGameStatistic.id_player")#, backref="player_stats")
    game = relationship("Game", lazy="noload", foreign_keys="PlayerGameStatistic.id_game")#, backref="game_stats")
    team = relationship("Team", lazy="noload", foreign_keys="PlayerGameStatistic.id_team")#, backref="team_player_stats")

    def __init__(self, team_id, game_id, player_id, min_play, fg, fga, fg_perc, three_pts, three_pts_att, three_pts_perc, 
                 ft, fta, ft_perc, offense_rebound, defense_rebound, total_rebound, assists, steals, blocks, turnovers,
                 personal_fouls, pts, plus_minor, active):
        self.id_team = team_id
        self.id_game = game_id
        self.id_player = player_id
        self.min_play = min_play
        self.fg = fg
        self.fga = fga
        self.fg_perc = fg_perc
        self.three_pts =three_pts
        self.three_pts_att = three_pts_att
        self.three_pts_perc = three_pts_perc
        self.ft = ft
        self.fta = fta
        self.ft_perc = ft_perc
        self.offense_rebound = offense_rebound
        self.defense_rebound =defense_rebound
        self.total_rebound = total_rebound
        self.assists = assists
        self.steals = steals
        self.blocks = blocks
        self.turnovers = turnovers
        self.personal_fouls = personal_fouls
        self.pts = pts
        self.plus_minos = plus_minor
        self.active = active

    def json(self):
       return {'Need to be implemented' + 'date': self.min_play.strftime('%H:%M')}\
