from sqlalchemy import create_engine, text, and_, update
from sqlalchemy.orm import sessionmaker, subqueryload, selectinload
from model.game import Game as game
from dao.player_game_statistics_dao import PlayerGameStatsDAO
from dao.game_dao import GameDAO
from dao.player_dao import PlayerDAO
from dao import dao
from scrapers.basketball_reference.br_game_scrap import BasketballReferenceGameScrap

class PlayersGamesStatisticsDBCreatorService():
    def __init__(self):
        pass
        #DAO.__init__(self)
        
    def createPlayersGamesStatisticsByGames(self):
        #GAmes without statistics
        games = GameDAO().listGamesWithoutStatistics()
        #Create update player statistic
        for game in games:
            dfVisitor, dfHome = BasketballReferenceGameScrap().callPage(game.gamehomepage, game.visit_team.code, game.home_team.code)
            for index, row in dfVisitor.iterrows():
                player = PlayerDAO.getPlayerByName(row['Starters'])
                PlayerGameStatsDAO.createOrUpdatePlayerGameStatistic(game.id_visit_team, game.id_game, player.id_player, )
                self, team_id, game_id, player_id, min_play, fg, fga, fg_perc, three_pts, three_pts_att, 
                                            three_pts_perc, ft, fta, ft_perc, offense_rebound, defense_rebound, total_rebound, 
                                            assists, steals, blocks, turnovers, personal_fouls, pts, plus_minos, active, ts_perc, 
                                            efg_perc, threepar_perc, ftr_perc, orb_perc, drb_perc, trb_perc, ast_perc, stl_perc, 
                                            blk_perc, tov_perc, usg_perc, or_tg, dr_tg, bpm
                PlayerGameStatsDAO.createOrUpdatePlayerGameStatistic(0,0,0,)
                #Starters         Tobias Harris
                #MP                       34:14
                #FG                           7
                #FGA                         14
                #FG%                       .500
                #3P                           3
                #3PA                          6
                #3P%                       .500
                #FT                           1
                #FTA                          2
                #FT%                       .500
                #ORB                          1
                #DRB                          1
                #TRB                          2
                #AST                          0
                #STL                          3
                #BLK                          0
                #TOV                          0
                #PF                           3
                #PTS                         18
                #+/-                         -1
                #efg_perc                  .607
                #threepar_perc             .429
                #ftr_perc                  .143
                #orb_perc                   4.1
                #drb_perc                   4.2
                #trb_perc                   4.2
                #ast_perc                   0.0
                #stl_perc                   4.3
                #blk_perc                   0.0
                #tov_perc                   0.0
                #usg_perc                  19.6
                #or_tg                      122
                #dr_tg                      125
                #bpm                        2.6

        return
    
    