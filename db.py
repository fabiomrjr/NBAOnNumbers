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
            Column('fg_perc', Integer),
            Column('three_pts', Integer),
            Column('three_pts_att', Integer),
            Column('three_pts_perc', Integer),
            Column('ft', Integer),
            Column('fta', Integer),
            Column('ft_perc', Integer),
            Column('offense_rebound', Integer),
            Column('defense_rebound', Integer),
            Column('total_rebound', Integer),
            Column('assists', Integer),
            Column('steals', Integer),
            Column('blocks', Integer),
            Column('turnovers', Integer),
            Column('personal_fouls', Integer),
            Column('pts', Integer),
            Column('plus_minos', Integer),
            Column('active', Boolean)
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

        #column = Column('macdsub', Float(precision=8))
        #column_name = column.compile(dialect=self.engine.dialect)
        #column_type = column.type.compile(self.engine.dialect)
        #self.engine.execute('ALTER TABLE %s ADD COLUMN %s %s' % ('candlesbyminute', column_name, column_type))
