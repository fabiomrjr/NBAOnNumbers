from scrapers.basketball_reference.br_league_scrap import BasketballReferenceLeagueScheduleScrap
#from scrapers.sportsbooks.betano_scrap import BasketballReferenceGameScrap
#from scrapers.nba.nba_schedule_scrap import NBAScheduleScrap

from dao.game_dao import GameDAO
from dao.team_dao import TeamDAO

from services.teams_db_creator_service import TeamsDBCreatorService
from services.games_db_creator_service import GamesDBCreatorService
from services.players_db_creator_service import PlayersDBCreatorService
from services.players_games_statistics_db_creator import PlayersGamesStatisticsDBCreatorService
from services.odds_db_creator_service import OddsDBCreatorService

from datetime import datetime as dt
from util import util
from db import db

#db().createTables()
#Prepar Teams
#TeamsDBCreatorService().createLeagueTeams()
#Prepar Players
#PlayersDBCreatorService().listPlayersHome()
#Prepar Games
#scheduledf = BasketballReferenceLeagueScheduleScrap().checkAllSchedule('/leagues/NBA_2023_games-april.html')
#GamesDBCreatorService().createGamesByScheduleDF(scheduledf)
#Otencao de Odds e correcao dos nomes dos times
OddsDBCreatorService.getAndSaveNHLOdds()
OddsDBCreatorService.getAndSaveNBAOdds()

startDate = dt.now()


endDate = dt.now()
print("Finish Schedule Dataframe. Seconds " + str((endDate - startDate).total_seconds()))
