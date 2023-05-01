from source.services.games.nba_games_db_creator_service import NBAGamesDBCreatorService
from source.services.games.nhl_games_db_creator_service import NHLGamesDBCreatorService
from source.services.games.mlb_games_db_creator_service import MLBGamesDBCreatorService

from datetime import datetime as dt

NBAGamesDBCreatorService().createNBAGames()
#NHLGamesDBCreatorService().createNHLGames()

#startDate = dt.now()
#MLBGamesDBCreatorService().createMLBGames()
#endDate = dt.now()
#print("Jogos MLB atualizados em seconds " + str((endDate - startDate).total_seconds()))
