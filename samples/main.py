from NFLScrapping.buildGame import BuildGame
from NFLScrapping.buildTeam import BuildTeam
from NFLScrapping.buildWeek import BuildWeek
from db import db
from datetime import datetime as dt
from NFLScrapping.builder.team_builder import TeamBuilder

db().createTables()

#TeamBuilder().createDefaultTeams()
#BuildTeam().check()

#array = BuildGame().check('https://www.pro-football-reference.com/boxscores/201909050chi.htm')


# start 1 and end 16 (Weeks)
games = BuildWeek().check('https://www.pro-football-reference.com/years/2010', 1, 2)

i = 0
total = len(games)
startDate = dt.now()
for gameItem in games:
    array = BuildGame().check(gameItem)
    i+=1
    print("Termina jogo " + str(i) + " de um total de " + str(total))

endDate = dt.now()
print("Finish Game Builder. Seconds " + str((endDate - startDate).total_seconds()))
