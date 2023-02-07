import config
from sqlalchemy import create_engine, text, and_
from sqlalchemy.orm import sessionmaker, subqueryload
from ..model.game import Game
from ..model.team_game_statistic import TeamGameStatistic
from ..dao.dao import DAO

class TeamGameStatsDAO(DAO):

    def __init__(self):
        DAO.__init__(self)

    def createTeamGameStats(self, team_id, game_id, first_downs, rush_att, rush_yds, rush_yds_tds, passing_compl, passing_att, passing_yds, passing_td,
                 passing_int, passing_sacks, passing_yds_lost, net_pass_yards, total_yards, fumbles, fumbles_lost, turnovers, penalties,
                 penalties_yards, third_down, third_down_convertion, fourth_down, fourth_down_convertion, time_of_possession_min):

        c1 = TeamGameStatistic(team_id, game_id, first_downs, rush_att, rush_yds, rush_yds_tds, passing_compl, passing_att, passing_yds, passing_td,
                 passing_int, passing_sacks, passing_yds_lost, net_pass_yards, total_yards, fumbles, fumbles_lost, turnovers, penalties,
                 penalties_yards, third_down, third_down_convertion, fourth_down, fourth_down_convertion, time_of_possession_min)

        try:
            self.session.add(c1)
            self.session.commit()
        except:
            self.session.rollback()
            raise
        return c1

    def getTeamGameStatsByTeamAndGAme(self, team_id, game_id):
        try:
            #stringText = "SELECT * FROM team_game_stats where id_team = " + str(team_id) + " and id_game = " + str(game_id)
            item = self.session.query(TeamGameStatistic).options(subqueryload(TeamGameStatistic.team_of_stats), subqueryload(TeamGameStatistic.game_of_stats)).filter(and_(TeamGameStatistic.id_team == int(team_id), TeamGameStatistic.id_game == int(game_id))).first()
        except:
            self.session.rollback()
            raise

        return item