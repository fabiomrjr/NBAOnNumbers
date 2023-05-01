import datetime

from source.dao.player_game_statistics_dao import PlayerGameStatsDAO
from source.dao.game_dao import GameDAO
from source.dao.player_dao import PlayerDAO
from source.scrapers.basketball_reference.br_nba_game_scrap import BasketballReferenceGameScrap

class PlayersGamesStatisticsDBCreatorService():
    def __init__(self):
        pass
        #DAO.__init__(self)
        
    def createPlayersGamesStatisticsByGames(self):
        #GAmes without statistics
        games = GameDAO().listGamesWithoutStatistics()
        #Create update player statistic
        self.createPlayerStatisticsByGames(games)
        
    def createPlayerStatisticsByGames(self, games):
        for game in games:
            dfVisitor, dfHome = BasketballReferenceGameScrap().callPage(game.gamehomepage, game.visit_team.code, game.home_team.code)
            
            for index, row in dfVisitor.iterrows():
                self.createPlayerStatistics(game, row)
                
            for index, row in dfHome.iterrows():
                self.createPlayerStatistics(game, row)
        return
    
    def createPlayerStatistics(self, game, row):
        if row['Starters'] == "Team Totals":
            active = False if row['MP'] == "0" else True
            mp_total_splitted = row['MP'].split(":")
            minutesPlayed = 0 if row['MP'] == "0" else datetime.time(0, int(mp_total_splitted[0]), int(mp_total_splitted[1]), 0)
            
            return None
        else:
            player = PlayerDAO().providePlayer(row['Starters'], "", 0, "")
            active = False if row['MP'] == "0" else True
            mp_total_splitted = row['MP'].split(":")
            minutesPlayed = 0 if row['MP'] == "0" else datetime.time(0, int(mp_total_splitted[0]), int(mp_total_splitted[1]), 0)
            
            playerStatistic = PlayerGameStatsDAO().createOrUpdatePlayerGameStatistic(game.id_visit_team, game.id_game, player.id_player, 
                                                                    minutesPlayed, int(row['FG']), int(row['FGA']), float(row['FG%']), int(row['3P']),
                                                                    int(row['3PA']), float(row['3P%']), int(row['FT']), int(row['FTA']), float(row['FT%']),
                                                                    int(row['ORB']), int(row['DRB']), int(row['TRB']), int(row['AST']), int(row['STL']),
                                                                    int(row['BLK']), int(row['TOV']), int(row['PF']), int(row['PTS']), row['+/-'], active, float(row['ts_perc']),
                                                                    float(row['efg_perc']), float(row['threepar_perc']), float(row['ftr_perc']),
                                                                    float(row['orb_perc']), float(row['drb_perc']), float(row['trb_perc']), 
                                                                    float(row['ast_perc']), float(row['stl_perc']), float(row['blk_perc']), 
                                                                    float(row['tov_perc']), float(row['usg_perc']), int(row['or_tg']), int(row['dr_tg']), float(row['bpm']))
        
        return playerStatistic
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
    
    