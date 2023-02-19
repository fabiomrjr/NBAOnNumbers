from scrapers.basketball_reference.br_league_scrap import BasketballReferenceLeagueScheduleScrap
#from scrapers.basketball_reference.br_game_scrap import BasketballReferenceGameScrap
#from scrapers.nba.nba_schedule_scrap import NBAScheduleScrap

from dao.game_dao import GameDAO
from dao.team_dao import TeamDAO

from services.teams_db_creator_service import TeamsDBCreatorService
from services.games_db_creator_service import GamesDBCreatorService
from services.players_db_creator_service import PlayersDBCreatorService

from datetime import datetime as dt
from util import util
from db import db

#db().createTables()
#TeamsDBCreatorService().createLeagueTeams()
#PlayersDBCreatorService().listPlayersHome()

#Prepare Dataframes
#Scheduel
startDate = dt.now()

#scheduledf = BasketballReferenceLeagueScheduleScrap().checkAllSchedule('/leagues/NBA_2023_games-december.html')
#GamesDBCreatorService().createGamesByScheduleDF(scheduledf)

scheduledf = BasketballReferenceLeagueScheduleScrap().checkAllSchedule('/leagues/NBA_2023_games-november.html')
GamesDBCreatorService().createGamesByScheduleDF(scheduledf)

endDate = dt.now()
print("Finish Schedule Dataframe. Seconds " + str((endDate - startDate).total_seconds()))
