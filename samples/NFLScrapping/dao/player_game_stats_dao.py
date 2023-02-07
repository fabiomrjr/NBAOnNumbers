import config
from sqlalchemy import create_engine, text, and_
from sqlalchemy.orm import sessionmaker, with_polymorphic, subqueryload
from ..model.game import Game
from ..model.team import Team
from ..model.player import Player
from ..model.player_game_statistic import PlayerGameStatistic
from ..model.player_game_offense_statistic import PlayerGameOffenseStatistic
from ..model.player_game_defense_statistic import PlayerGameDefenseStatistic
from ..dao.dao import DAO

class PlayerGameStatsDAO(DAO):

    def __init__(self):
        DAO.__init__(self)

    def createOffensePlayerGameStats(self, team_id, game_id, player_id, passing_compl, passing_att, passing_yds, passing_td, passing_int, passing_sacks, passing_yds_lost, passing_longest_compl,
                 rate, rushing_att, rushing_yds, rushing_td, rushing_longest, receiving_target, receiving_receptions, receiving_yds, receiving_td,
                 receiving_longest, fumbles, fumbles_lost):

        c1 = PlayerGameOffenseStatistic(team_id, game_id, player_id, passing_compl, passing_att, passing_yds, passing_td, passing_int, passing_sacks, passing_yds_lost, passing_longest_compl,
                 rate, rushing_att, rushing_yds, rushing_td, rushing_longest, receiving_target, receiving_receptions, receiving_yds, receiving_td,
                 receiving_longest, fumbles, fumbles_lost)

        try:
            self.session.add(c1)
            self.session.commit()
        except:
            self.session.rollback()
            raise
        return c1

    def createDiffensePlayerGameStats(self, team_id, game_id, player_id, defense_int, defense_int_yds, defense_int_tds, defense_int_long_return,
                 defense_pass_def, sacks, tackles_comb, tackles_solo, tackles_ast, tackles_for_lost, tackles_qb_hits,
                 fumbles_recovery, fumbles_yds, fumbles_td, fumbles_forced):

        c1 = PlayerGameDefenseStatistic(team_id, game_id, player_id, defense_int, defense_int_yds, defense_int_tds, defense_int_long_return,
                 defense_pass_def, sacks, tackles_comb, tackles_solo, tackles_ast, tackles_for_lost, tackles_qb_hits,
                 fumbles_recovery, fumbles_yds, fumbles_td, fumbles_forced)

        try:
            self.session.add(c1)
            self.session.commit()
        except:
            self.session.rollback()
            raise
        return c1

    def getPlayerGameStatsByPlayerTeamAndGame(self, team_id, game_id, player_id):
        try:
            #stringText = "SELECT * FROM player_game_stats where id_team = " + str(team_id) + " and id_game = " + str(game_id) + " and id_player = " + str(player_id)
            offense_plus_diffense = with_polymorphic(PlayerGameStatistic, [PlayerGameOffenseStatistic, PlayerGameDefenseStatistic])
            item = self.session.query(offense_plus_diffense).\
                options(subqueryload(offense_plus_diffense.PlayerGameOffenseStatistic.team), subqueryload(offense_plus_diffense.PlayerGameOffenseStatistic.game), subqueryload(offense_plus_diffense.PlayerGameOffenseStatistic.player)).\
                filter(and_(offense_plus_diffense.player.has(Player.id_player == int(player_id)), offense_plus_diffense.team.has(Team.id_team == int(team_id)), offense_plus_diffense.game.has(Game.id_game == int(game_id)))).first()
        except:
            self.session.rollback()
            raise

        return item