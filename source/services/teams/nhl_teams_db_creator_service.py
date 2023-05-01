from source.dao.team_dao import TeamDAO

class NHLTeamsDBCreatorService():
    def __init__(self):
        pass
        
    def createLeagueTeams(self):
        TeamDAO().createOrUpdateTeams("Anaheim Ducks","ANA","Anaheim","Ducks","","Pacific","Western Conference","NHL")
        TeamDAO().createOrUpdateTeams("Arizona Coyotes","ARI","Arizona","Coyotes","","Central","Western Conference","NHL")
        TeamDAO().createOrUpdateTeams("Boston Bruins","BOS","Boston","Bruins","","Atlantic","Eastern Conference","NHL")
        TeamDAO().createOrUpdateTeams("Buffalo Sabres","BUF","Buffalo","Sabres","","Atlantic","Eastern Conference","NHL")
        TeamDAO().createOrUpdateTeams("Carolina Hurricanes","CAR","Carolina","Hurricanes","","Metropolitan","Eastern Conference","NHL")
        TeamDAO().createOrUpdateTeams("Columbus Blue Jackets","CBJ","Columbus","Blue Jackets","","Metropolitan","Eastern Conference","NHL")
        TeamDAO().createOrUpdateTeams("Calgary Flames","CGY","Calgary","Flames","","Pacific","Western Conference","NHL")
        TeamDAO().createOrUpdateTeams("Chicago Blackhawks","CHI","Chicago","Blackhawks","","Central","Western Conference","NHL")
        TeamDAO().createOrUpdateTeams("Colorado Avalanche","COL","Colorado","Avalanche","","Central","Western Conference","NHL")
        TeamDAO().createOrUpdateTeams("Dallas Stars","DAL","Dallas","Stars","","Central","Western Conference","NHL")
        TeamDAO().createOrUpdateTeams("Detroit Red Wings","DET","Detroit","Red Wings","","Atlantic","Eastern Conference","NHL")
        TeamDAO().createOrUpdateTeams("Edmonton Oilers","EDM","Edmonton","Oilers","","Pacific","Western Conference","NHL")
        TeamDAO().createOrUpdateTeams("Florida Panthers","FLA","Florida","Panthers","","Atlantic","Eastern Conference","NHL")
        TeamDAO().createOrUpdateTeams("Los Angeles Kings","LAK","Los Angeles","Kings","","Pacific","Western Conference","NHL")
        TeamDAO().createOrUpdateTeams("Minnesota Wild","MIN","Minnesota","Wild","","Central","Western Conference","NHL")
        TeamDAO().createOrUpdateTeams("Montreal Canadiens","MTL","Montreal","Canadiens","","Atlantic","Eastern Conference","NHL")
        TeamDAO().createOrUpdateTeams("New Jersey Devils","NJD","New Jersey","Devils","","Metropolitan","Eastern Conference","NHL")
        TeamDAO().createOrUpdateTeams("Nashville Predators","NSH","Nashville","Predators","","Central","Western Conference","NHL")
        TeamDAO().createOrUpdateTeams("New York Islanders","NYI","New York","Islanders","","Metropolitan","Eastern Conference","NHL")
        TeamDAO().createOrUpdateTeams("New York Rangers","NYR","New York","Rangers","","Metropolitan","Eastern Conference","NHL")
        TeamDAO().createOrUpdateTeams("Ottawa Senators","OTT","Ottawa","Senators","","Atlantic","Eastern Conference","NHL")
        TeamDAO().createOrUpdateTeams("Philadelphia Flyers","PHI","Philadelphia","Flyers","","Metropolitan","Eastern Conference","NHL")
        TeamDAO().createOrUpdateTeams("Pittsburgh Penguins","PIT","Pittsburgh","Penguins","","Metropolitan","Eastern Conference","NHL")
        TeamDAO().createOrUpdateTeams("Seattle Kraken","SEA","Seattle","Kraken","","Pacific","Western Conference","NHL")
        TeamDAO().createOrUpdateTeams("San Jose Sharks","SJS","San Jose","Sharks","","Pacific","Western Conference","NHL")
        TeamDAO().createOrUpdateTeams("St. Louis Blues","STL","St. Louis","Blues","","Central","Western Conference","NHL")
        TeamDAO().createOrUpdateTeams("Tampa Bay Lightning","TBL","Tampa Bay","Lightning","","Atlantic","Eastern Conference","NHL")
        TeamDAO().createOrUpdateTeams("Toronto Maple Leafs","TOR","Toronto","Maple Leafs","","Atlantic","Eastern Conference","NHL")
        TeamDAO().createOrUpdateTeams("Vancouver Canucks","VAN","Vancouver","Canucks","","Pacific","Western Conference","NHL")
        TeamDAO().createOrUpdateTeams("Vegas Golden Knights","VEG","Vegas","Golden Knights","","Pacific","Western Conference","NHL")
        TeamDAO().createOrUpdateTeams("Winnipeg Jets","WPG","Winnipeg","Jets","","Central","Western Conference","NHL")
        TeamDAO().createOrUpdateTeams("Washington Capitals","WSH","Washington","Capitals","","Metropolitan","Eastern Conference","NHL")
        
