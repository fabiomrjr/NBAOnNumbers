import config
from sqlalchemy import create_engine, text, and_, update
from sqlalchemy.orm import sessionmaker, with_polymorphic, subqueryload
from model.game import Game
from model.team import Team
from model.player import Player
from model.player_game_statistic import PlayerGameStatistic
from .dao import DAO

class PlayerGameStatsDAO():

    def __init__(self):
        pass
        #DAO.__init__(self)

    def createPlayerGameStatistics(self, team_id, game_id, player_id, min_play, fg, fga, fg_perc, three_pts, three_pts_att, three_pts_perc, 
                 ft, fta, ft_perc, offense_rebound, defense_rebound, total_rebound, assists, steals, blocks, turnovers,
                 personal_fouls, pts, plus_minor, active):
        dao = DAO()
        dao.startConnection()
        
        c1 = PlayerGameStatistic(team_id, game_id, player_id, min_play, fg, fga, fg_perc, three_pts, three_pts_att, three_pts_perc, 
                 ft, fta, ft_perc, offense_rebound, defense_rebound, total_rebound, assists, steals, blocks, turnovers,
                 personal_fouls, pts, plus_minor, active)

        try:
            dao.session.add(c1)
            dao.session.commit()
        except:
            dao.session.rollback()
            raise
        dao.quitConnection()
        return c1

    def getPlayerGameStatsByPlayerTeamAndGame(self, team_id, game_id, player_id):
        dao = DAO()
        dao.startConnection()
        
        try:
            item = dao.session.query(PlayerGameStatistic).filter(and_(PlayerGameStatistic.id_game == game_id, 
                                                                      PlayerGameStatistic.id_team == team_id, 
                                                                      PlayerGameStatistic.id_player == player_id)).first()
        except:
            dao.session.rollback()
            raise
        dao.quitConnection()
        return item
    
    def updatePlayerGameStatistic(self, id_player_game_statistic, min_play, fg, fga, fg_perc, three_pts, three_pts_att, three_pts_perc, 
                 ft, fta, ft_perc, offense_rebound, defense_rebound, total_rebound, assists, steals, blocks, turnovers,
                 personal_fouls, pts, plus_minor, active):
        dao = DAO()
        dao.startConnection()

        try:
            stmt = (update(PlayerGameStatistic).where(PlayerGameStatistic.id_player_game_statistic == id_player_game_statistic)
                    .values(min_play = min_play, fg = fg, fga = fga, fg_perc = fg_perc, three_pts = three_pts, 
                            three_pts_att = three_pts_att, three_pts_perc = three_pts_perc, ft = ft, fta = fta, 
                            ft_perc = ft_perc, offense_rebound = offense_rebound, defense_rebound = defense_rebound, 
                            total_rebound = total_rebound, assists = assists, steals = steals, blocks = blocks, 
                            turnovers = turnovers,personal_fouls = personal_fouls, pts = pts, plus_minor = plus_minor, 
                            active = active))
            dao.session.execute(stmt)
            dao.session.commit()
            item = dao.session.query(PlayerGameStatistic).filter(PlayerGameStatistic.id_player_game_statistic == id_player_game_statistic).first()
        except:
            dao.session.rollback()            
            raise
        dao.quitConnection()

        return item
    
    def createOrUpdatePlayerGameStatistic(self, team_id, game_id, player_id, min_play, fg, fga, fg_perc, three_pts, three_pts_att, three_pts_perc, 
                 ft, fta, ft_perc, offense_rebound, defense_rebound, total_rebound, assists, steals, blocks, turnovers,
                 personal_fouls, pts, plus_minor, active):
        
        PlayerGameStatistic = self.getPlayerGameStatsByPlayerTeamAndGame(team_id, game_id, player_id)
        
        if PlayerGameStatistic != None:
            return self.updatePlayerGameStatistic(PlayerGameStatistic.id_player_game_statistic, min_play, fg, fga, fg_perc, three_pts, three_pts_att, three_pts_perc, 
                 ft, fta, ft_perc, offense_rebound, defense_rebound, total_rebound, assists, steals, blocks, turnovers,
                 personal_fouls, pts, plus_minor, active)
        
        return self.createPlayerGameStatistics(team_id, game_id, player_id, min_play, fg, fga, fg_perc, three_pts, three_pts_att, three_pts_perc, 
                 ft, fta, ft_perc, offense_rebound, defense_rebound, total_rebound, assists, steals, blocks, turnovers,
                 personal_fouls, pts, plus_minor, active)