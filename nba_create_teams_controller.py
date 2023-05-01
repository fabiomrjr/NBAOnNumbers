from source.services.teams.nba_teams_db_creator_service import NBATeamsDBCreatorService
from source.services.teams.nhl_teams_db_creator_service import NHLTeamsDBCreatorService
from source.services.teams.mlb_teams_db_creator_service import MLBTeamsDBCreatorService
from datetime import datetime as dt

startDate = dt.now()

NBATeamsDBCreatorService().createLeagueTeams()
NHLTeamsDBCreatorService().createLeagueTeams()
MLBTeamsDBCreatorService().createLeagueTeams()

endDate = dt.now()
print("NBA criacao de times em seconds " + str((endDate - startDate).total_seconds()))
