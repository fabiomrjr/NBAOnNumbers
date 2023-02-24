import config
from sqlalchemy import create_engine, MetaData, Column, Integer, Float, Table, DateTime, String, Boolean, TIME
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class db():
    def __init__(self):
        self.engine = create_engine(config.connectionString)
        self.meta = MetaData()

    def createTables(self):

        player = Table(
            'player', self.meta,
            Column('id_player', Integer, primary_key=True, autoincrement=True),
            Column('name', String(50)),
            Column('position', String(10)),
            Column('number', Integer),
            Column('player_nba_link', String(60))
        )

        team = Table(
            'team', self.meta,
            Column('id_team', Integer, primary_key=True, autoincrement=True),
            Column('full_name', String(50)),
            Column('code', String(20)),
            Column('city_name', String(50)),
            Column('name', String(80)),
            Column('homepage', String(80)),
            Column('division', String(50)),
            Column('conference', String(50))
        )

        game = Table(
            'game', self.meta,
            Column('id_game', Integer, primary_key=True, autoincrement=True),
            Column('id_visit_team', Integer),
            Column('id_home_team', Integer),
            #Column('id_winner_team', Integer),
            #Column('id_predic_winner', Integer),
            Column('date', DateTime),
            Column('home_score', Integer),
            Column('visit_score', Integer),
            Column('gamehomepage', String(80)),
            Column('has_overtime', Boolean),
            Column('attend', Integer),
            Column('arena', String(50))
        )

        player_game_statistic = Table(
            'player_game_statistic', self.meta,
            Column('id_player_game_statistic', Integer, primary_key=True, autoincrement=True),
            Column('id_player', Integer),
            Column('id_game', Integer),
            Column('id_team', Integer),
            Column('min_play', TIME),
            Column('fg', Integer),
            Column('fga', Integer),
            Column('fg_perc', Float(precision=3)),#FG%
            Column('three_pts', Integer),#3P
            Column('three_pts_att', Integer),#3PA
            Column('three_pts_perc', Float(precision=3)),#3P%
            Column('ft', Integer),
            Column('fta', Integer),
            Column('ft_perc', Float(precision=3)),
            Column('offense_rebound', Integer),#ORB
            Column('defense_rebound', Integer),#DRB
            Column('total_rebound', Integer),#TRB
            Column('assists', Integer),#AST
            Column('steals', Integer),#STL
            Column('blocks', Integer),#BLK
            Column('turnovers', Integer),#TOV
            Column('personal_fouls', Integer),#PF
            Column('pts', Integer),
            Column('plus_minos', Integer),#+/-
            Column('active', Boolean),
            #Advanced
            Column('ts_perc', Float(precision=3)),
            Column('efg_perc', Float(precision=3)),
            Column('threepar_perc', Float(precision=3)),
            Column('ftr_perc', Float(precision=3)),
            Column('orb_perc', Float(precision=3)),
            Column('drb_perc', Float(precision=3)),
            Column('trb_perc', Float(precision=3)),
            Column('ast_perc', Float(precision=3)),
            Column('stl_perc', Float(precision=3)),
            Column('blk_perc', Float(precision=3)),
            Column('tov_perc', Float(precision=3)),
            Column('usg_perc', Float(precision=3)),
            Column('or_tg', Integer),
            Column('dr_tg', Integer),
            Column('bpm', Float(precision=3))
        )

        team_game_statistic = Table(
            'team_game_statistic', self.meta,
            Column('id_team_game_statistic', Integer, primary_key=True, autoincrement=True),
            Column('id_team', Integer),
            Column('id_game', Integer),
            # Estatisticas dos times
            Column('q1_score', Integer),
            Column('q2_score', Integer),
            Column('q3_score', Integer),
            Column('q4_score', Integer),
            Column('half_score', Integer),
            Column('total_score', Integer),
            Column('turnover', Integer)
        )

        analysis_team_game = Table(
            'analysis_team_game', self.meta,
            Column('id_analysis_team_game', Integer, primary_key=True, autoincrement=True),
            Column('id_game', Integer),
            Column('id_team', Integer)
            #Campos a serem analisados time
        )
        
        analysis_player_game = Table(
            'analysis_player_game', self.meta,
            Column('id_analysis_team_game', Integer, primary_key=True, autoincrement=True),
            Column('id_game', Integer),
            Column('id_player', Integer),
            Column('pts_media', Integer)
            #Campos a serem analisados jogadores
        )
        
        odds = Table(
            'odds', self.meta,
            Column('id_odd', Integer, primary_key=True, autoincrement=True),
            Column('id_game', Integer),
            Column('game_date', DateTime),
            Column('date', DateTime),
            Column('league', String(5)),
            Column('visitor_team_name', String(80)),
            Column('home_team_name', String(80)),
            Column('visitor_win_odd', Float(precision=2)),
            Column('home_win_odd', Float(precision=2)),
            Column('visitor_spread', Float(precision=2)),
            Column('home_spread', Float(precision=2)),
            Column('visitor_win_spread', Float(precision=2)),
            Column('home_win_spread', Float(precision=2)),
            Column('total', Float(precision=2)),
            Column('total_under', Float(precision=2)),
            Column('total_upper', Float(precision=2))
        )
        self.meta.create_all(self.engine)
