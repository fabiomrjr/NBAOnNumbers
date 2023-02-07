from util import util
import pandas as pd
from datetime import datetime as dt

from ..dao.game_dao import GameDAO
from ..dao.team_dao import TeamDAO
from ..dao.team_game_stats_dao import TeamGameStatsDAO
from ..dao.player_game_stats_dao import PlayerGameStatsDAO
from ..dao.player_property_dao import PlayerPropertyDAO

class GameBuilder():

    def __init__(self):
        pass

    def createGame(self, dayGame, startTime, gameDF, coach_home, coach_visit, score_home, score_visit, offenseDF, diffenseDF):

        gameDateTime = util().getDateTimeByDayAndTime(dayGame, startTime)
        home_team = TeamDAO().getTeamByCode(str(gameDF.columns[2]))
        visit_team = TeamDAO().getTeamByCode(str(gameDF.columns[1]))
        if score_home != "":
            homer_score = int(score_home)
        else:
            homer_score = None

        if score_visit != "":
            visitor_score = int(score_visit)
        else:
            visitor_score = None

        game = GameDAO().getGameByTeamsAndDateTime(home_team.id_team, visit_team.id_team, gameDateTime)
        if game == None:
            if homer_score > visitor_score:
                game = GameDAO().createGame(home_team.id_team, visit_team.id_team, gameDateTime, homer_score, home_team.id_team)
            elif homer_score < visitor_score:
                game = GameDAO().createGame(home_team.id_team, visit_team.id_team, gameDateTime, homer_score, visit_team.id_team)
            else:
                game = GameDAO().createGame(home_team.id_team, visit_team.id_team, gameDateTime, homer_score, None)

        self.createTeamsGameStats(game, gameDF, home_team, visit_team)
        self.createOffensePlayersStats(game, offenseDF)
        self.createDefensePlayersStats(game, diffenseDF)

    def createDefensePlayersStats(self, game, diffenseDF):
        for i in range(0, len(diffenseDF)):
            player_name = diffenseDF.values[i][0]
            player_team_code = diffenseDF.values[i][1]

            if pd.isna(player_name) or player_name == "Player":
                continue

            playerProperty = PlayerPropertyDAO().getPlayerPropertyByPlayerNameAndTeamCode(player_team_code, player_name)

            if not playerProperty == None:
                playerStatsGame = PlayerGameStatsDAO().getPlayerGameStatsByPlayerTeamAndGame(playerProperty.id_team, game.id_game, playerProperty.id_player)

                if playerStatsGame == None:
                    defense_int = 0 if pd.isna(diffenseDF.values[i][2]) else int(diffenseDF.values[i][2])
                    defense_int_yds = 0 if pd.isna(diffenseDF.values[i][3]) else int(diffenseDF.values[i][3])
                    defense_int_tds = 0 if pd.isna(diffenseDF.values[i][4]) else int(diffenseDF.values[i][4])
                    defense_int_long_return = 0 if pd.isna(diffenseDF.values[i][5]) else int(diffenseDF.values[i][5])
                    defense_pass_def = 0 if pd.isna(diffenseDF.values[i][6]) else int(diffenseDF.values[i][6])
                    sacks = 0.0 if pd.isna(diffenseDF.values[i][7]) else float(diffenseDF.values[i][7])
                    tackles_comb = 0 if pd.isna(diffenseDF.values[i][8]) else int(diffenseDF.values[i][8])
                    tackles_solo = 0 if pd.isna(diffenseDF.values[i][9]) else int(diffenseDF.values[i][9])
                    tackles_ast = 0 if pd.isna(diffenseDF.values[i][10]) else int(diffenseDF.values[i][10])
                    tackles_for_lost = 0 if pd.isna(diffenseDF.values[i][11]) else int(diffenseDF.values[i][11])
                    tackles_qb_hits = 0 if pd.isna(diffenseDF.values[i][12]) else int(diffenseDF.values[i][12])
                    fumbles_recovery = 0 if pd.isna(diffenseDF.values[i][13]) else int(diffenseDF.values[i][13])
                    fumbles_yds = 0 if pd.isna(diffenseDF.values[i][14]) else int(diffenseDF.values[i][14])
                    fumbles_td = 0 if pd.isna(diffenseDF.values[i][15]) else int(diffenseDF.values[i][15])
                    fumbles_forced = 0 if pd.isna(diffenseDF.values[i][16]) else int(diffenseDF.values[i][16])

                    playerStatsGame = PlayerGameStatsDAO().createDiffensePlayerGameStats(playerProperty.id_team,
                                                                                        game.id_game,
                                                                                        playerProperty.id_player, defense_int, defense_int_yds, defense_int_tds, defense_int_long_return,
                                                                                        defense_pass_def, sacks, tackles_comb, tackles_solo, tackles_ast, tackles_for_lost,
                                                                                        tackles_qb_hits, fumbles_recovery, fumbles_yds, fumbles_td, fumbles_forced)

    def createOffensePlayersStats(self, game, offenseDF):
        for i in range(0, len(offenseDF)):
            player_name = offenseDF.values[i][0]
            player_team_code = offenseDF.values[i][1]

            if pd.isna(player_name) or player_name == "Player":
                continue

            playerProperty = PlayerPropertyDAO().getPlayerPropertyByPlayerNameAndTeamCode(player_team_code, player_name)

            if not playerProperty == None:
                playerStatsGame = PlayerGameStatsDAO().getPlayerGameStatsByPlayerTeamAndGame(playerProperty.id_team,
                                                                                             game.id_game,
                                                                                             playerProperty.id_player)

                if playerStatsGame == None:
                    rate = 0.0 if pd.isna(offenseDF.values[i][10]) else float(offenseDF.values[i][10])
                    pass_comp = 0 if pd.isna(offenseDF.values[i][2]) else int(offenseDF.values[i][2])
                    pass_att = 0 if pd.isna(offenseDF.values[i][3]) else int(offenseDF.values[i][3])
                    pass_yds = 0 if pd.isna(offenseDF.values[i][4]) else int(offenseDF.values[i][4])
                    pass_tds = 0 if pd.isna(offenseDF.values[i][5]) else int(offenseDF.values[i][5])
                    pass_int = 0 if pd.isna(offenseDF.values[i][6]) else int(offenseDF.values[i][6])
                    sacks = 0 if pd.isna(offenseDF.values[i][7]) else int(offenseDF.values[i][7])
                    sack_yds_lost = 0 if pd.isna(offenseDF.values[i][8]) else int(offenseDF.values[i][8])
                    pass_long_yds = 0 if pd.isna(offenseDF.values[i][9]) else int(offenseDF.values[i][9])
                    rush_att = 0 if pd.isna(offenseDF.values[i][11]) else int(offenseDF.values[i][11])
                    rush_yds = 0 if pd.isna(offenseDF.values[i][12]) else int(offenseDF.values[i][12])
                    rush_tds = 0 if pd.isna(offenseDF.values[i][13]) else int(offenseDF.values[i][13])
                    rush_long_yds = 0 if pd.isna(offenseDF.values[i][14]) else int(offenseDF.values[i][14])
                    receiving_target = 0 if pd.isna(offenseDF.values[i][15]) else int(offenseDF.values[i][15])
                    receiving_receptions = 0 if pd.isna(offenseDF.values[i][16]) else int(offenseDF.values[i][16])
                    receiving_yds = 0 if pd.isna(offenseDF.values[i][17]) else int(offenseDF.values[i][17])
                    receiving_tds = 0 if pd.isna(offenseDF.values[i][18]) else int(offenseDF.values[i][18])
                    receiving_long_yds = 0 if pd.isna(offenseDF.values[i][19]) else int(offenseDF.values[i][19])
                    fumbles = 0 if pd.isna(offenseDF.values[i][20]) else int(offenseDF.values[i][20])
                    fumbles_lost = 0 if pd.isna(offenseDF.values[i][21]) else int(offenseDF.values[i][21])

                    playerStatsGame = PlayerGameStatsDAO().createOffensePlayerGameStats(playerProperty.id_team,
                                                                                        game.id_game,
                                                                                        playerProperty.id_player,
                                                                                        pass_comp, pass_att, pass_yds,
                                                                                        pass_tds, pass_int, sacks,
                                                                                        sack_yds_lost, pass_long_yds,
                                                                                        rate, rush_att, rush_yds,
                                                                                        rush_tds, rush_long_yds,
                                                                                        receiving_target,
                                                                                        receiving_receptions,
                                                                                        receiving_yds, receiving_tds,
                                                                                        receiving_long_yds, fumbles,
                                                                                        fumbles_lost)

    def createTeamsGameStats(self, game, gameDF, home_team, visit_team):

        team_statistic = TeamGameStatsDAO().getTeamGameStatsByTeamAndGAme(home_team.id_team, game.id_game)

        if team_statistic == None:
            first_downs = int(gameDF.values[0][2])
            rush_att = int(gameDF.values[1][2].split("-")[0])
            rush_yds = int(gameDF.values[1][2].split("-")[1])
            rush_yds_tds = int(gameDF.values[1][2].split("-")[2])
            passing_compl = int(gameDF.values[2][2].split("-")[0])
            passing_att = int(gameDF.values[2][2].split("-")[1])
            passing_yds = int(gameDF.values[2][2].split("-")[2])
            passing_td = int(gameDF.values[2][2].split("-")[3])
            passing_int = int(gameDF.values[2][2].split("-")[4])
            passing_sacks = int(gameDF.values[3][2].split("-")[0])
            passing_yds_lost = int(gameDF.values[3][2].split("-")[1])
            net_pass_yards = int(gameDF.values[4][2])
            total_yards = int(gameDF.values[5][2])
            fumbles = int(gameDF.values[6][2].split("-")[0])
            fumbles_lost = int(gameDF.values[6][2].split("-")[1])
            turnovers = int(gameDF.values[7][2])
            penalties = int(gameDF.values[8][2].split("-")[0])
            penalties_yards = int(gameDF.values[8][2].split("-")[1])
            third_down = int(gameDF.values[9][2].split("-")[0])
            third_down_convertion = int(gameDF.values[9][2].split("-")[1])
            fourth_down = int(gameDF.values[10][2].split("-")[0])
            fourth_down_convertion = int(gameDF.values[10][2].split("-")[1])
            time_of_possession_min = float(gameDF.values[11][2].split(":")[0]) + float(gameDF.values[11][2].split(":")[1]) / 60

            team_statistic = TeamGameStatsDAO().createTeamGameStats(home_team.id_team, game.id_game, first_downs, rush_att, rush_yds, rush_yds_tds, passing_compl,
                                                                    passing_att, passing_yds, passing_td, passing_int, passing_sacks, passing_yds_lost,
                                                                    net_pass_yards, total_yards, fumbles, fumbles_lost, turnovers, penalties,
                                                                    penalties_yards, third_down, third_down_convertion, fourth_down, fourth_down_convertion,
                                                                    time_of_possession_min)
            
        team_statistic2 = TeamGameStatsDAO().getTeamGameStatsByTeamAndGAme(visit_team.id_team, game.id_game)

        if team_statistic2 == None:
            first_downs = int(gameDF.values[0][1])
            rush_att = int(gameDF.values[1][1].split("-")[0])
            rush_yds = int(gameDF.values[1][1].split("-")[1])
            rush_yds_tds = int(gameDF.values[1][1].split("-")[2])
            passing_compl = int(gameDF.values[2][1].split("-")[0])
            passing_att = int(gameDF.values[2][1].split("-")[1])
            passing_yds = int(gameDF.values[2][1].split("-")[2])
            passing_td = int(gameDF.values[2][1].split("-")[3])
            passing_int = int(gameDF.values[2][1].split("-")[4])
            passing_sacks = int(gameDF.values[3][1].split("-")[0])
            passing_yds_lost = int(gameDF.values[3][1].split("-")[1])
            net_pass_yards = int(gameDF.values[4][1])
            total_yards = int(gameDF.values[5][1])
            fumbles = int(gameDF.values[6][1].split("-")[0])
            fumbles_lost = int(gameDF.values[6][1].split("-")[1])
            turnovers = int(gameDF.values[7][1])
            penalties = int(gameDF.values[8][1].split("-")[0])
            penalties_yards = int(gameDF.values[8][1].split("-")[1])
            third_down = int(gameDF.values[9][1].split("-")[0])
            third_down_convertion = int(gameDF.values[9][1].split("-")[1])
            fourth_down = int(gameDF.values[10][1].split("-")[0])
            fourth_down_convertion = int(gameDF.values[10][1].split("-")[1])
            time_of_possession_min = float(gameDF.values[11][1].split(":")[0]) + float(gameDF.values[11][1].split(":")[1]) / 60

            team_statistic2 = TeamGameStatsDAO().createTeamGameStats(visit_team.id_team, game.id_game, first_downs, rush_att, rush_yds, rush_yds_tds, passing_compl,
                                                                    passing_att, passing_yds, passing_td, passing_int, passing_sacks, passing_yds_lost,
                                                                    net_pass_yards, total_yards, fumbles, fumbles_lost, turnovers, penalties,
                                                                    penalties_yards, third_down, third_down_convertion, fourth_down, fourth_down_convertion,
                                                                    time_of_possession_min)







