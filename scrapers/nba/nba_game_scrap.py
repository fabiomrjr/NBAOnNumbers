import requests
import re
import numpy as np
import pandas as pd

from datetime import datetime as dt
from bs4 import BeautifulSoup, Comment

def checkAllSchedule():
    x = ['games?date=2023-02-06'
            ]
    dtFinal = pd.DataFrame()
    #for month in x:
    pageBS = callPage("https://www.nba.com/games?date=2023-02-09")
    #pageBS = callPage("https://www.nba.com/games?date=2023-02-21") # no games
    #pageBS = callPage("https://www.nba.com/games?date=2023-02-24) # agendados
    
    df1 = extractTable(pageBS)
    dtFinal = dtFinal.append(df1)
    #print(df1)
    return dtFinal

def callPage(url):
    req = requests.get(url)
    content = ''
    if req.status_code == 200:
        print('Requisição bem sucedida! Day at NBA !')
        content = req.content

    pageBS = BeautifulSoup(content, 'html.parser')
    return pageBS

def extractTable(pageBS):
    
    teams = pageBS.find_all('span', attrs={'class':'MatchupCardTeamName_teamName__9YaBA'})
    records = pageBS.find_all('p', attrs={'class':'MatchupCardTeamRecord_record__20YHe'})
    placar = pageBS.find_all('p', attrs={'class':'MatchupCardScore_p__dfNvc GameCardMatchup_matchupScoreCard__owb6w'})
    print(teams)
    print(records)
    #Jogos Ja jogados
    #Teams = <span class="MatchupCardTeamName_teamName__9YaBA">Nuggets</span>
    #record = <p class="MatchupCardTeamRecord_record__20YHe">38-18</p>
    #Placar = <p class="MatchupCardScore_p__dfNvc GameCardMatchup_matchupScoreCard__owb6w">115<svg xmlns="http://www.w3.org/2000/svg" width="7" height="12" viewBox="0 0 7 12" class="GameCardMatchup_homeWin__5E_iM GameCardMatchup_won__89eVM" data-no-icon="right" role="presentation"><path fill="currentColor" fill-rule="nonzero" d="M.5 6l6 5.5V.5z"></path></svg></p>
    #Jogo = section "GameCard_gcMain__q1lUW"
    #
    #Agendados
    #<section class="GameCard_gcMain__q1lUW"><a href="/game/atl-vs-cha-0022200857" class="GameCard_gcm__SKtfh GameCardMatchup_gameCardMatchup__H0uPe"><div class="GameCardMatchup_wrapper__uUdW8"><article class="GameCardMatchup_article__Fsvx9"><figure class="MatchupCardTeamLogo_base__WZl01 GameCardMatchup_matchupCardTeamLogo__ZqZXC" style="width: 52px; height: 52px;"><div class="TeamLogo_block__rSWmO"><img src="https://cdn.nba.com/logos/nba/1610612737/global/L/logo.svg" title=" Logo" alt=" Logo" class="TeamLogo_logo__PclAJ" loading="lazy"></div></figure><div class="MatchupCardTeamName_base__PBkuX" data-team-id="1610612737"><span class="MatchupCardTeamName_teamName__9YaBA">Hawks</span></div><p class="MatchupCardTeamRecord_record__20YHe">29-28</p></article><div class="GameCardMatchup_statusWrapper__TDbQz"><div class="GameCardMatchup_gameCardMatchupStatusWrapper__8rQ8v"><div class="GameCardMatchupStatusText_gcs__2yfjE" data-is-preseason="false" data-game-status="1"><p class="GameCardMatchupStatusText_gcsText__PcQUX">7:00 pm ET</p></div><p class="GameCardMatchup_showBroadcasters__B7lu2">LEAGUE PASS</p></div></div><article class="GameCardMatchup_article__Fsvx9"><figure class="MatchupCardTeamLogo_base__WZl01 GameCardMatchup_matchupCardTeamLogo__ZqZXC" style="width: 52px; height: 52px;"><div class="TeamLogo_block__rSWmO"><img src="https://cdn.nba.com/logos/nba/1610612766/global/L/logo.svg" title=" Logo" alt=" Logo" class="TeamLogo_logo__PclAJ" loading="lazy"></div></figure><div class="MatchupCardTeamName_base__PBkuX" data-team-id="1610612766"><span class="MatchupCardTeamName_teamName__9YaBA">Hornets</span></div><p class="MatchupCardTeamRecord_record__20YHe">15-43</p></article></div></a><ul class="Tabs_tab__rnewb" data-show-border="true"><li class="TabLink_tab__uKOPj"><a href="/game/atl-vs-cha-0022200857" class="Anchor_anchor__cSc3P TabLink_link__f_15h" data-is-external="false" data-has-more="false" data-has-children="true" data-track="click" data-type="cta" data-id="nba:games:main:preview:cta" data-text="PREVIEW" data-content="ATL @ CHA, 2023-02-13" data-content-id="0022200857" data-section="games">PREVIEW</a></li><li class="TabLink_tab__uKOPj" data-track="click" data-type="cta" data-id="nba:games:main:tickets:cta" data-text="TICKETS" data-content="ATL @ CHA, 2023-02-13" data-content-id="0022200857" data-section="games" rel="noopener"><a href="https://a.data.nba.com/tickets/single/2022/0022200857/LEAG_GAMELINE" class="Anchor_anchor__cSc3P TabLink_link__f_15h" data-is-external="false" data-has-more="false" data-has-children="true" rel="noopener noreferrer nofollow" target="_blank">TICKETS</a></li></ul></section>
    #teams <div class="MatchupCardTeamName_base__PBkuX" data-team-id="1610612737"><span class="MatchupCardTeamName_teamName__9YaBA">Hawks</span></div>
    #record <p class="MatchupCardTeamRecord_record__20YHe">29-28</p>
    #preview = <a href="/game/atl-vs-cha-0022200857" class="Anchor_anchor__cSc3P TabLink_link__f_15h" data-is-external="false" data-has-more="false" data-has-children="true" data-track="click" data-type="cta" data-id="nba:games:main:preview:cta" data-text="PREVIEW" data-content="ATL @ CHA, 2023-02-13" data-content-id="0022200857" data-section="games">PREVIEW</a>
    ##table = soup.find_all('table', attrs={'class':'teams'})
    
    boxScoreTable = pageBS.find_all('a', attrs={'class':'Anchor_anchor__cSc3P TabLink_link__f_15h'})
    
    for item in boxScoreTable:
        lineDataBS = BeautifulSoup(str(item.extract()), 'html.parser')
        value = lineDataBS.get_text()
        if value == "BOX SCORE":
            result = re.search('href="(.*)"', str(lineDataBS))
            print(result.group(1))

startDate = dt.now()
df = checkAllSchedule()
#gamedf = NBAScheduleScrap().checkAllSchedule()
#leagueScheduledf = BasketballReferenceLeagueScheduleScrap().checkAllSchedule()

##for link in leagueScheduledf.get('BoxScoreLink'):
##    gamedf = GameScrap().check(link)
#gamedf = BasketballReferenceGameScrap().check("/boxscores/202210180GSW.html")

endDate = dt.now()
print("Finish Game Builder. Seconds " + str((endDate - startDate).total_seconds()))