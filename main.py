from scrapers.basketball_reference.br_league_scrap import BasketballReferenceLeagueScheduleScrap
from scrapers.basketball_reference.br_game_scrap import BasketballReferenceGameScrap
from scrapers.nba.nba_schedule_scrap import NBAScheduleScrap
from datetime import datetime as dt
from util import util

#db().createTables()

startDate = dt.now()
gamedf = NBAScheduleScrap().checkAllSchedule()
#leagueScheduledf = BasketballReferenceLeagueScheduleScrap().checkAllSchedule()

##for link in leagueScheduledf.get('BoxScoreLink'):
##    gamedf = GameScrap().check(link)
#gamedf = BasketballReferenceGameScrap().check("/boxscores/202210180GSW.html")

endDate = dt.now()
print("Finish Game Builder. Seconds " + str((endDate - startDate).total_seconds()))
