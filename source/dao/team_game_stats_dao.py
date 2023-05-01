import resources.config as config
from sqlalchemy import create_engine, text, and_, update
from sqlalchemy.orm import sessionmaker, with_polymorphic, subqueryload
from source.model.team_game_statistic import TeamGameStatistic
from source.dao.dao import DAO

class TeamGameStatsDAO(DAO):

    def __init__(self):
        DAO.__init__(self)

    def getTeamGameStatsByTeamAndGAme(self, team_id, game_id):
        try:
            #stringText = "SELECT * FROM team_game_stats where id_team = " + str(team_id) + " and id_game = " + str(game_id)
            item = self.session.query(TeamGameStatistic).options(subqueryload(TeamGameStatistic.team_of_stats), subqueryload(TeamGameStatistic.game_of_stats)).filter(and_(TeamGameStatistic.id_team == int(team_id), TeamGameStatistic.id_game == int(game_id))).first()
        except:
            self.session.rollback()
            raise

        return item
    
    def createTeamGameStatistics(self, team_id, game_id, q1_score,q2_score, q3_score, q4_score, half_score, total_score, turnover, min_play, fg, fga, fg_perc, three_pts, 
                                 three_pts_att, three_pts_perc, ft, fta, ft_perc, offense_rebound, defense_rebound, total_rebound, assists, steals, blocks, turnovers, 
                                 personal_fouls, pts, plus_minos, ts_perc, efg_perc, threepar_perc, ftr_perc, orb_perc, drb_perc, trb_perc, ast_perc, stl_perc, 
                                 blk_perc, tov_perc, usg_perc, or_tg, dr_tg, bpm):
        dao = DAO(config.connectionStringNBA)
        dao.startConnection()
        
        c1 = TeamGameStatistic(self, team_id, game_id, q1_score,q2_score, q3_score, q4_score, half_score, total_score, turnover, min_play, fg, fga, fg_perc, three_pts, 
                               three_pts_att, three_pts_perc, ft, fta, ft_perc, offense_rebound, defense_rebound, total_rebound, assists, steals, blocks, turnovers, 
                               personal_fouls, pts, plus_minos, ts_perc, efg_perc, threepar_perc, ftr_perc, orb_perc, drb_perc, trb_perc, ast_perc, stl_perc, blk_perc, 
                               tov_perc, usg_perc, or_tg, dr_tg, bpm)

        try:
            dao.session.add(c1)
            dao.session.commit()
        except:
            dao.session.rollback()
            raise
        dao.quitConnection()
        return c1

    def getTeamGameStatsByTeamAndGame(self, team_id, game_id):
        dao = DAO(config.connectionStringNBA)
        dao.startConnection()
        
        try:
            item = dao.session.query(TeamGameStatistic).filter(and_(TeamGameStatistic.id_game == game_id, 
                                                                      TeamGameStatistic.id_team == team_id)).first()
        except:
            dao.session.rollback()
            raise
        dao.quitConnection()
        return item
    
    def updateTeamGameStatistic(self, id_team_game_statistic, q1_score, q2_score, q3_score, q4_score, half_score, total_score, turnover, min_play, fg, fga, fg_perc, three_pts, 
                               three_pts_att, three_pts_perc, ft, fta, ft_perc, offense_rebound, defense_rebound, total_rebound, assists, steals, blocks, turnovers, 
                               personal_fouls, pts, plus_minos, ts_perc, efg_perc, threepar_perc, ftr_perc, orb_perc, drb_perc, trb_perc, ast_perc, stl_perc, blk_perc, 
                               tov_perc, usg_perc, or_tg, dr_tg, bpm):
        dao = DAO(config.connectionStringNBA)
        dao.startConnection()

        try:
            stmt = (update(TeamGameStatistic).where(TeamGameStatistic.id_team_game_statistic == id_team_game_statistic)
                    .values(q1_score = q1_score, q2_score = q2_score, q3_score = q3_score, q4_score = q4_score, half_score = half_score, total_score = total_score, 
                            turnover = turnover, min_play = min_play, fg = fg, fga = fga, fg_perc = fg_perc, three_pts = three_pts, 
                            three_pts_att = three_pts_att, three_pts_perc = three_pts_perc, ft = ft, fta = fta, 
                            ft_perc = ft_perc, offense_rebound = offense_rebound, defense_rebound = defense_rebound, 
                            total_rebound = total_rebound, assists = assists, steals = steals, blocks = blocks, 
                            turnovers = turnovers,personal_fouls = personal_fouls, pts = pts, plus_minos = plus_minos, ts_perc = ts_perc, efg_perc = efg_perc, threepar_perc = threepar_perc, ftr_perc = ftr_perc,
                            orb_perc = orb_perc, drb_perc = drb_perc, trb_perc = trb_perc, ast_perc = ast_perc, stl_perc = stl_perc, blk_perc = blk_perc,
                            tov_perc = tov_perc, usg_perc = usg_perc, or_tg = or_tg, dr_tg = dr_tg, bpm = bpm))
            dao.session.execute(stmt)
            dao.session.commit()
            item = dao.session.query(TeamGameStatistic).filter(TeamGameStatistic.id_team_game_statistic == id_team_game_statistic).first()
        except:
            dao.session.rollback()            
            raise
        dao.quitConnection()

        return item
    
    def createOrUpdateTeamGameStatistic(self, team_id, game_id, q1_score, q2_score, q3_score, q4_score, half_score, total_score, turnover, min_play, fg, fga, fg_perc, three_pts, 
                                 three_pts_att, three_pts_perc, ft, fta, ft_perc, offense_rebound, defense_rebound, total_rebound, assists, steals, blocks, turnovers, 
                                 personal_fouls, pts, plus_minos, ts_perc, efg_perc, threepar_perc, ftr_perc, orb_perc, drb_perc, trb_perc, ast_perc, stl_perc, 
                                 blk_perc, tov_perc, usg_perc, or_tg, dr_tg, bpm):
        
        TeamGameStatisticItem = self.getTeamGameStatsByTeamAndGame(team_id, game_id)
        
        if TeamGameStatisticItem != None:
            return self.updateTeamGameStatistic(TeamGameStatisticItem.id_team_game_statistic, q1_score,q2_score, q3_score, q4_score, half_score, total_score, turnover, min_play, fg, fga, fg_perc, three_pts, 
                                 three_pts_att, three_pts_perc, ft, fta, ft_perc, offense_rebound, defense_rebound, total_rebound, assists, steals, blocks, turnovers, 
                                 personal_fouls, pts, plus_minos, ts_perc, efg_perc, threepar_perc, ftr_perc, orb_perc, drb_perc, trb_perc, ast_perc, stl_perc, 
                                 blk_perc, tov_perc, usg_perc, or_tg, dr_tg, bpm)
        
        return self.createTeamGameStatistics(team_id, game_id, q1_score,q2_score, q3_score, q4_score, half_score, total_score, turnover, min_play, fg, fga, fg_perc, three_pts, 
                                 three_pts_att, three_pts_perc, ft, fta, ft_perc, offense_rebound, defense_rebound, total_rebound, assists, steals, blocks, turnovers, 
                                 personal_fouls, pts, plus_minos, ts_perc, efg_perc, threepar_perc, ftr_perc, orb_perc, drb_perc, trb_perc, ast_perc, stl_perc, 
                                 blk_perc, tov_perc, usg_perc, or_tg, dr_tg, bpm)