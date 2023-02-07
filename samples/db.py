import config
from sqlalchemy import create_engine, MetaData, Column, Integer, Float, Table, DateTime, String, Boolean
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
            Column('active', Boolean),
            Column('status', String(5))
        )

        team = Table(
            'team', self.meta,
            Column('id_team', Integer, primary_key=True, autoincrement=True),
            Column('full_name', String(50)),
            Column('code', String(20)),
            Column('city_name', String(50)),
            Column('name', String(80)),
            Column('homepage', String(80))
        )

        game = Table(
            'game', self.meta,
            Column('id_game', Integer, primary_key=True, autoincrement=True),
            Column('id_visit_team', Integer),
            Column('id_home_team', Integer),
            Column('id_winner_team', Integer),
            Column('id_predic_winner', Integer),
            Column('date', DateTime),
            Column('home_score', Integer),
            Column('visit_score', Integer)
        )

        player_statistic = Table(
            'player_statistic', self.meta,
            Column('id_player_statistic', Integer, primary_key=True, autoincrement=True),
            Column('id_team_player', Integer),
            Column('passing_compl', Integer),
            Column('passing_att', Integer),
            Column('passing_yds', Integer),
            Column('passing_td', Integer),
            Column('passing_int', Integer),
            Column('passing_sacks', Integer),
            Column('passing_yds_lost', Integer),
            Column('passing_longest_compl', Integer),
            Column('rate', Float(precision=2)),
            Column('rushing_att', Integer),
            Column('rushing_yds', Integer),
            Column('rushing_td', Integer),
            Column('rushing_longest', Integer),
            Column('receiving_target', Integer),
            Column('receiving_receptions', Integer),
            Column('receiving_yds', Integer),
            Column('receiving_td', Integer),
            Column('receiving_longest', Integer),
            Column('fumbles', Integer),
            Column('fumbles_lost', Integer)
        )

        player_game_statistic = Table(
            'player_game_statistic', self.meta,
            Column('id_player_game_statistic', Integer, primary_key=True, autoincrement=True),
            Column('id_player', Integer),
            Column('id_team', Integer),
            Column('id_game', Integer)
        )

        player_game_offense_statistic = Table(
            'player_game_offense_statistic', self.meta,
            Column('id_player_game_statistic', Integer, primary_key=True, autoincrement=True),
            Column('passing_compl', Integer),
            Column('passing_att', Integer),
            Column('passing_yds', Integer),
            Column('passing_td', Integer),
            Column('passing_int', Integer),
            Column('passing_sacks', Integer),
            Column('passing_yds_lost', Integer),
            Column('passing_longest_compl', Integer),
            Column('rate', Float(precision=2)),
            Column('rushing_att', Integer),
            Column('rushing_yds', Integer),
            Column('rushing_td', Integer),
            Column('rushing_longest', Integer),
            Column('receiving_target', Integer),
            Column('receiving_receptions', Integer),
            Column('receiving_yds', Integer),
            Column('receiving_td', Integer),
            Column('receiving_longest', Integer),
            Column('fumbles', Integer),
            Column('fumbles_lost', Integer)
        )

        player_game_defense_statistic = Table(
            'player_game_defense_statistic', self.meta,
            Column('id_player_game_statistic', Integer, primary_key=True, autoincrement=True),
            Column('defense_int', Integer),
            Column('defense_int_yds', Integer),
            Column('defense_int_tds', Integer),
            Column('defense_int_long_return', Integer),
            Column('defense_pass_def', Integer),
            Column('sacks', Float(precision=2)),
            Column('tackles_comb', Integer),
            Column('tackles_solo', Integer),
            Column('tackles_ast', Integer),
            Column('tackles_for_lost', Integer),
            Column('tackles_qb_hits', Integer),
            Column('fumbles_recovery', Integer),
            Column('fumbles_yds', Integer),
            Column('fumbles_td', Integer),
            Column('fumbles_forced', Integer)
        )

        team_statistic = Table(
            'team_game_statistic', self.meta,
            Column('id_team_statistic', Integer, primary_key=True, autoincrement=True),
            Column('id_team', Integer),
            Column('id_game', Integer),
            Column('first_downs', Integer),
            Column('rush_att', Integer),
            Column('rush_yds', Integer),
            Column('rush_yds_tds', Integer),
            Column('passing_compl', Integer),
            Column('passing_att', Integer),
            Column('passing_yds', Integer),
            Column('passing_td', Integer),
            Column('passing_int', Integer),
            Column('passing_sacks', Integer),
            Column('passing_yds_lost', Integer),
            Column('net_pass_yards', Integer),
            Column('total_yards', Integer),
            Column('fumbles', Integer),
            Column('fumbles_lost', Integer),
            Column('turnovers', Integer),
            Column('penalties', Integer),
            Column('penalties_yards', Integer),
            Column('third_down', Integer),
            Column('third_down_convertion', Integer),
            Column('fourth_down', Integer),
            Column('fourth_down_convertion', Integer),
            Column('time_of_possession_min', Float(precision=2))
        )

        player_property = Table(
            'player_property', self.meta,
            Column('id_player_team_property', Integer, primary_key=True, autoincrement=True),
            Column('id_player', Integer),
            Column('id_team', Integer),
            Column('date_hire', DateTime),
            Column('date_fire', DateTime),
            Column('active', Boolean)
        )

        self.meta.create_all(self.engine)

        #column = Column('macdsub', Float(precision=8))
        #column_name = column.compile(dialect=self.engine.dialect)
        #column_type = column.type.compile(self.engine.dialect)
        #self.engine.execute('ALTER TABLE %s ADD COLUMN %s %s' % ('candlesbyminute', column_name, column_type))
