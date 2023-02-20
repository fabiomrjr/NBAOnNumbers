from sqlalchemy import create_engine, text, and_, update
from sqlalchemy.orm import sessionmaker, subqueryload, selectinload
from model.game import Game as game
from dao.player_game_statistics_dao import PlayerGameStatsDAO
from dao.game_dao import GameDAO
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
            BasketballReferenceGameScrap().callPage(game.gamehomepage, game.visit_team.code, game.home_team.code)
            PlayerGameStatsDAO.createOrUpdatePlayerGameStatistic()
        return
    
    