from source.dao.team_dao import TeamDAO

class NBATeamsDBCreatorService():
    def __init__(self):
        pass
        
    def createLeagueTeams(self):
        TeamDAO().createOrUpdateTeams("Boston Celtics", "BOS", "Boston", "Celtics", "team/1610612738/celtics", "Atlantic", "Eastern Conference", "NBA")
        TeamDAO().createOrUpdateTeams("Brooklyn Nets", "BKN", "Brooklyn", "Nets", "team/1610612751/nets", "Atlantic", "Eastern Conference", "NBA")
        TeamDAO().createOrUpdateTeams("New York Knicks", "NYK", "New York", "Knicks", "team/1610612752/knicks", "Atlantic", "Eastern Conference", "NBA")
        TeamDAO().createOrUpdateTeams("Philadelphia 76ers", "PHI", "Philadelphia", "76ers", "team/1610612755/sixers", "Atlantic", "Eastern Conference", "NBA")
        TeamDAO().createOrUpdateTeams("Toronto Raptors", "TOR", "Toronto", "Raptors", "team/1610612761/raptors", "Atlantic", "Eastern Conference", "NBA")
        
        TeamDAO().createOrUpdateTeams("Chicago Bulls", "CHI", "Chicago", "Bulls", "team/1610612741/bulls", "Central", "Eastern Conference", "NBA")
        TeamDAO().createOrUpdateTeams("Cleveland Cavaliers", "CLE", "Cleveland", "Cavaliers", "team/1610612739/cavaliers", "Central", "Eastern Conference", "NBA")
        TeamDAO().createOrUpdateTeams("Detroit Pistons", "DET", "Detroit", "Pistons", "team/1610612765/pistons", "Central", "Eastern Conference", "NBA")
        TeamDAO().createOrUpdateTeams("Indiana Pacers", "IND", "Indiana", "Pacers", "team/1610612754/pacers", "Central", "Eastern Conference", "NBA")
        TeamDAO().createOrUpdateTeams("Milwaukee Bucks", "MIL", "Milwaukee", "Bucks", "team/1610612749/bucks", "Central", "Eastern Conference", "NBA")

        TeamDAO().createOrUpdateTeams("Atlanta Hawks", "ATL", "Atlanta", "Hawks", "team/1610612737/hawks", "Southeast", "Eastern Conference", "NBA")
        TeamDAO().createOrUpdateTeams("Charlotte Hornets", "CHA", "Charlotte", "Hornets", "team/1610612766/hornets", "Southeast", "Eastern Conference", "NBA")
        TeamDAO().createOrUpdateTeams("Miami Heat", "MIA", "Miami", "Heat", "team/1610612748/heat", "Southeast", "Eastern Conference", "NBA")
        TeamDAO().createOrUpdateTeams("Orlando Magic", "ORL", "Orlando", "Magic", "team/1610612753/magic", "Southeast", "Eastern Conference", "NBA")
        TeamDAO().createOrUpdateTeams("Washington Wizards", "WAS", "Washington", "Wizards", "team/1610612764/wizards", "Southeast", "Eastern Conference", "NBA")
        
        TeamDAO().createOrUpdateTeams("Denver Nuggets", "DEN", "Denver", "Nuggets", "team/1610612743/nuggets", "Northwest", "Western Conference", "NBA")
        TeamDAO().createOrUpdateTeams("Minnesota Timberwolves", "MIN", "Minnesota", "Timberwolves", "team/1610612750/timberwolves", "Northwest", "Western Conference", "NBA")
        TeamDAO().createOrUpdateTeams("Oklahoma City Thunder", "OKC", "Oklahoma City", "Thunder", "team/1610612760/thunder", "Northwest", "Western Conference", "NBA")
        TeamDAO().createOrUpdateTeams("Portland Trail Blazers", "PHI", "Portland", "Trail Blazers", "team/1610612757/blazers", "Northwest", "Western Conference", "NBA")
        TeamDAO().createOrUpdateTeams("Utah Jazz", "UTA", "Utah", "Jazz", "team/1610612762/jazz", "Northwest", "Western Conference", "NBA")
        
        TeamDAO().createOrUpdateTeams("Golden State Warriors", "GSW", "Golden State", "Warriors", "team/1610612744/warriors", "Pacific", "Western Conference", "NBA")
        TeamDAO().createOrUpdateTeams("Los Angeles Clippers", "LAC", "Los Angeles", "Clippers", "team/1610612746/clippers", "Pacific", "Western Conference", "NBA")
        TeamDAO().createOrUpdateTeams("Los Angeles Lakers", "LAL", "Los Angeles", "Lakers", "team/1610612747/lakers", "Pacific", "Western Conference", "NBA")
        TeamDAO().createOrUpdateTeams("Phoenix Suns", "PHX", "Phoenix", "Suns", "team/1610612756/suns", "Pacific", "Western Conference", "NBA")
        TeamDAO().createOrUpdateTeams("Sacramento Kings", "SAC", "Sacramento", "Kings", "team/1610612758/kings", "Pacific", "Western Conference", "NBA")

        TeamDAO().createOrUpdateTeams("Dallas Mavericks", "DAL", "Dallas", "Mavericks", "team/1610612742/mavericks", "Southwest", "Western Conference", "NBA")
        TeamDAO().createOrUpdateTeams("Houston Rockets", "HOU", "Houston", "Rockets", "team/1610612745/rockets", "Southwest", "Western Conference", "NBA")
        TeamDAO().createOrUpdateTeams("Memphis Grizzlies", "MEM", "Memphis", "Grizzlies", "team/1610612763/grizzlies", "Southwest", "Western Conference", "NBA")
        TeamDAO().createOrUpdateTeams("New Orleans Pelicans", "NOP", "New Orleans", "Pelicans", "team/1610612740/pelicans", "Southwest", "Western Conference", "NBA")
        TeamDAO().createOrUpdateTeams("San Antonio Spurs", "SAS", "San Antonio", "Spurs", "team/1610612759/spurs", "Southwest", "Western Conference", "NBA")

