from source.services.odds.odds_db_creator_service import OddsDBCreatorService
from source.services.odds.odds_db_creator_service import OddsDBCreatorService
from datetime import datetime as dt

#startDate = dt.now()
#OddsDBCreatorService().getAndSaveNBAOdds()
#endDate = dt.now()
#print("NBA Odds obtidas em seconds " + str((endDate - startDate).total_seconds()))


startDate = dt.now() 
OddsDBCreatorService().getAndSaveNHLOdds()
endDate = dt.now()
print("NHL Odds obtidas em seconds " + str((endDate - startDate).total_seconds()))
