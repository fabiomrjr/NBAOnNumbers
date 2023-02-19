import config
from sqlalchemy import create_engine, text, and_, update
from sqlalchemy.orm import sessionmaker, subqueryload, selectinload
from model.game import Game as game
from dao.team_dao import TeamDAO
from dao.game_dao import GameDAO
from dao import dao

class TeamsDBCreatorService():
    def __init__(self):
        pass
        
    def createLeagueTeams(self):
        TeamDAO().createOrUpdateTeams("Boston Celtics", "BOS", "Boston", "Celtics", "team/1610612738/celtics", "Atlantic", "Eastern Conference")
        TeamDAO().createOrUpdateTeams("Brooklyn Nets", "BKN", "Brooklyn", "Nets", "team/1610612751/nets", "Atlantic", "Eastern Conference")
        TeamDAO().createOrUpdateTeams("New York Knicks", "NYK", "New York", "Knicks", "team/1610612752/knicks", "Atlantic", "Eastern Conference")
        TeamDAO().createOrUpdateTeams("Philadelphia 76ers", "PHI", "Philadelphia", "76ers", "team/1610612755/sixers", "Atlantic", "Eastern Conference")
        TeamDAO().createOrUpdateTeams("Toronto Raptors", "TOR", "Toronto", "Raptors", "team/1610612761/raptors", "Atlantic", "Eastern Conference")
        
        TeamDAO().createOrUpdateTeams("Chicago Bulls", "CHI", "Chicago", "Bulls", "team/1610612741/bulls", "Central", "Eastern Conference")
        TeamDAO().createOrUpdateTeams("Cleveland Cavaliers", "CLE", "Cleveland", "Cavaliers", "team/1610612739/cavaliers", "Central", "Eastern Conference")
        TeamDAO().createOrUpdateTeams("Detroit Pistons", "DET", "Detroit", "Pistons", "team/1610612765/pistons", "Central", "Eastern Conference")
        TeamDAO().createOrUpdateTeams("Indiana Pacers", "IND", "Indiana", "Pacers", "team/1610612754/pacers", "Central", "Eastern Conference")
        TeamDAO().createOrUpdateTeams("Milwaukee Bucks", "MIL", "Milwaukee", "Bucks", "team/1610612749/bucks", "Central", "Eastern Conference")

        TeamDAO().createOrUpdateTeams("Atlanta Hawks", "ATL", "Atlanta", "Hawks", "team/1610612737/hawks", "Southeast", "Eastern Conference")
        TeamDAO().createOrUpdateTeams("Charlotte Hornets", "CHA", "Charlotte", "Hornets", "team/1610612766/hornets", "Southeast", "Eastern Conference")
        TeamDAO().createOrUpdateTeams("Miami Heat", "MIA", "Miami", "Heat", "team/1610612748/heat", "Southeast", "Eastern Conference")
        TeamDAO().createOrUpdateTeams("Orlando Magic", "ORL", "Orlando", "Magic", "team/1610612753/magic", "Southeast", "Eastern Conference")
        TeamDAO().createOrUpdateTeams("Washington Wizards", "WAS", "Washington", "Wizards", "team/1610612764/wizards", "Southeast", "Eastern Conference")
        
        TeamDAO().createOrUpdateTeams("Denver Nuggets", "DEN", "Denver", "Nuggets", "team/1610612743/nuggets", "Northwest", "Western Conference")
        TeamDAO().createOrUpdateTeams("Minnesota Timberwolves", "MIN", "Minnesota", "Timberwolves", "team/1610612750/timberwolves", "Northwest", "Western Conference")
        TeamDAO().createOrUpdateTeams("Oklahoma City Thunder", "OKC", "Oklahoma City", "Thunder", "team/1610612760/thunder", "Northwest", "Western Conference")
        TeamDAO().createOrUpdateTeams("Portland Trail Blazers", "PHI", "Portland", "Trail Blazers", "team/1610612757/blazers", "Northwest", "Western Conference")
        TeamDAO().createOrUpdateTeams("Utah Jazz", "UTA", "Utah", "Jazz", "team/1610612762/jazz", "Northwest", "Western Conference")
        
        TeamDAO().createOrUpdateTeams("Golden State Warriors", "GSW", "Golden State", "Warriors", "team/1610612744/warriors", "Pacific", "Western Conference")
        TeamDAO().createOrUpdateTeams("LA Clippers", "LAC", "Los Angeles", "Clippers", "team/1610612746/clippers", "Pacific", "Western Conference")
        TeamDAO().createOrUpdateTeams("Los Angeles Lakers", "LAL", "Los Angeles", "Lakers", "team/1610612747/lakers", "Pacific", "Western Conference")
        TeamDAO().createOrUpdateTeams("Phoenix Suns", "PHX", "Phoenix", "Suns", "team/1610612756/suns", "Pacific", "Western Conference")
        TeamDAO().createOrUpdateTeams("Sacramento Kings", "SAC", "Sacramento", "Kings", "team/1610612758/kings", "Pacific", "Western Conference")

        TeamDAO().createOrUpdateTeams("Dallas Mavericks", "DAL", "Dallas", "Mavericks", "team/1610612742/mavericks", "Southwest", "Western Conference")
        TeamDAO().createOrUpdateTeams("Houston Rockets", "HOU", "Houston", "Rockets", "team/1610612745/rockets", "Southwest", "Western Conference")
        TeamDAO().createOrUpdateTeams("Memphis Grizzlies", "MEM", "Memphis", "Grizzlies", "team/1610612763/grizzlies", "Southwest", "Western Conference")
        TeamDAO().createOrUpdateTeams("New Orleans Pelicans", "NOP", "New Orleans", "Pelicans", "team/1610612740/pelicans", "Southwest", "Western Conference")
        TeamDAO().createOrUpdateTeams("San Antonio Spurs", "SAS", "San Antonio", "Spurs", "team/1610612759/spurs", "Southwest", "Western Conference")

