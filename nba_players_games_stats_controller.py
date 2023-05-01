from source.services.players.players_games_statistics_db_creator import PlayersGamesStatisticsDBCreatorService
from source.services.games.nhl_games_db_creator_service import NHLGamesDBCreatorService
from source.services.games.mlb_games_db_creator_service import MLBGamesDBCreatorService
from source.dao.game_dao import GameDAO

from datetime import datetime as dt

#games = GameDAO().listGamesWithoutStatistics()

startDate = dt.now()
PlayersGamesStatisticsDBCreatorService().createPlayersGamesStatisticsByGames()
endDate = dt.now()
print("Players Stats NBA criados/atualizados em seconds " + str((endDate - startDate).total_seconds()))
