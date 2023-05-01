from source.dao.team_dao import TeamDAO

class MLBTeamsDBCreatorService():
    def __init__(self):
        pass
        
    def createLeagueTeams(self):
        TeamDAO().createOrUpdateTeams("Tampa Bay Rays","","Tampa Bay", "Rays", "", "AL", "East Division", "MLB")
        TeamDAO().createOrUpdateTeams("Baltimore Orioles","","Baltimore", "Orioles", "", "AL", "East Division", "MLB")
        TeamDAO().createOrUpdateTeams("Boston Red Sox","","Boston", "Red Sox", "", "AL", "East Division", "MLB")
        TeamDAO().createOrUpdateTeams("New York Yankees","", "New York", "Yankees", "", "AL", "East Division", "MLB")
        TeamDAO().createOrUpdateTeams("Toronto Blue Jays","", "Toronto", "Blue Jays", "", "AL", "East Division", "MLB")
        TeamDAO().createOrUpdateTeams("Minnesota Twins","","Minnesota","Twins", "", "AL", "Central Division", "MLB")
        TeamDAO().createOrUpdateTeams("Cleveland Guardians","","Cleveland", "Guardians", "", "AL", "Central Division", "MLB")
        TeamDAO().createOrUpdateTeams("Chicago White Sox","", "Chicago", "White Sox", "", "AL", "Central Division", "MLB")
        TeamDAO().createOrUpdateTeams("Detroit Tigers","","Detroit","Tigers", "", "AL", "Central Division", "MLB")
        TeamDAO().createOrUpdateTeams("Kansas City Royals","","Kansas City","Royals", "", "AL", "Central Division", "MLB")
        TeamDAO().createOrUpdateTeams("Texas Rangers","","Texas","Rangers", "","AL", "West Division", "MLB")
        TeamDAO().createOrUpdateTeams("Houston Astros","","Houston","Astros", "", "AL", "West Division", "MLB")
        TeamDAO().createOrUpdateTeams("Los Angeles Angels", "", "Los Angeles","Angels", "", "AL", "West Division", "MLB")
        TeamDAO().createOrUpdateTeams("Oakland Athletics","","Oakland","Athletics", "", "AL", "West Division", "MLB")
        TeamDAO().createOrUpdateTeams("Seattle Mariners","","Seattle","Mariners", "", "AL", "West Division", "MLB")
        TeamDAO().createOrUpdateTeams("Atlanta Braves","","Atlanta","Braves", "", "NL", "East Division", "MLB")
        TeamDAO().createOrUpdateTeams("New York Mets","","New York","Mets", "", "NL", "East Division", "MLB")
        TeamDAO().createOrUpdateTeams("Miami Marlins","","Miami","Marlins", "", "NL", "East Division", "MLB")
        TeamDAO().createOrUpdateTeams("Philadelphia Phillies","","Philadelphia","Phillies", "", "NL", "East Division", "MLB")
        TeamDAO().createOrUpdateTeams("Washington Nationals","","Washington","Nationals", "", "NL", "East Division", "MLB")
        TeamDAO().createOrUpdateTeams("Chicago Cubs","","Chicago","Cubs", "", "NL", "Central Division", "MLB")
        TeamDAO().createOrUpdateTeams("Cincinnati Reds","","Cincinnati","Reds", "", "NL", "Central Division", "MLB")
        TeamDAO().createOrUpdateTeams("Milwaukee Brewers","","Milwaukee","Brewers", "", "NL", "Central Division", "MLB")
        TeamDAO().createOrUpdateTeams("Pittsburgh Pirates","","Pittsburgh", "Pirates", "", "NL", "Central Division", "MLB")
        TeamDAO().createOrUpdateTeams("St. Louis Cardinals","","St. Louis", "Cardinals", "", "NL", "Central Division", "MLB")
        TeamDAO().createOrUpdateTeams("Colorado Rockies","","Colorado", "Rockies", "", "NL", "West Division", "MLB")
        TeamDAO().createOrUpdateTeams("Los Angeles Dodgers","","Los Angeles","Dodgers", "", "NL", "West Division", "MLB")
        TeamDAO().createOrUpdateTeams("San Francisco Giants","","San Francisco","Giants", "", "NL", "West Division", "MLB")
        TeamDAO().createOrUpdateTeams("Arizona Diamondbacks","","Arizona","Diamondbacks", "", "NL", "West Division", "MLB")
        TeamDAO().createOrUpdateTeams("San Diego Padres", "","San Diego","Padres", "", "NL", "West Division", "MLB")

        

