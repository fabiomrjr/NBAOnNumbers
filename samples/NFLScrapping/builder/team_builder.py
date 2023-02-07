from ..dao.team_dao import TeamDAO

class TeamBuilder():

    def __init__(self):
        pass

    def createDefaultTeams(self):

        team = TeamDAO().getTeamByCode("NWE")
        if team == None:
            TeamDAO().createTeam("New England Patriots", "NWE", "New England", "Patriots", "teams/nwe/ANOXX_roster.htm")

        team = TeamDAO().getTeamByCode("GNB")
        if team == None:
            TeamDAO().createTeam("Green Bay Packers", "GNB", "Green Bay", "Packers", "teams/gnb/ANOXX_roster.htm")

        team = TeamDAO().getTeamByCode("CHI")
        if team == None:
            TeamDAO().createTeam("Chicago Bears", "CHI", "Chicago", "Bears", "teams/chi/ANOXX_roster.htm")

        team = TeamDAO().getTeamByCode("CAR")
        if team == None:
            TeamDAO().createTeam("Carolina Panthers", "CAR", "Carolina", "Panthers", "teams/car/ANOXX_roster.htm")

        team = TeamDAO().getTeamByCode("LAR")
        if team == None:
            TeamDAO().createTeam("Los Angeles Rams", "LAR;STL", "Los Angeles", "Rams", "teams/ram/ANOXX_roster.htm")

        team = TeamDAO().getTeamByCode("ARI")
        if team == None:
            TeamDAO().createTeam("Arizona Cardinals", "ARI;CRD", "Arizona", "Cardinals", "teams/crd/ANOXX_roster.htm")

        team = TeamDAO().getTeamByCode("CLE")
        if team == None:
            TeamDAO().createTeam("Cleveland Browns", "CLE", "Cleveland", "Browns", "teams/cle/ANOXX_roster.htm")

        team = TeamDAO().getTeamByCode("TEN")
        if team == None:
            TeamDAO().createTeam("Tennessee Titans", "TEN;OTI", "Tennessee", "Titans", "teams/oti/ANOXX_roster.htm")

        team = TeamDAO().getTeamByCode("DET")
        if team == None:
            TeamDAO().createTeam("Detroit Lions", "DET", "Detroit", "Lions", "teams/det/ANOXX_roster.htm")

        team = TeamDAO().getTeamByCode("DAL")
        if team == None:
            TeamDAO().createTeam("Dallas Cowboys", "DAL", "Dallas", "Cowboys", "teams/dal/ANOXX_roster.htm")

        team = TeamDAO().getTeamByCode("NYG")
        if team == None:
            TeamDAO().createTeam("New York Giants", "NYG", "New York", "Giants", "teams/nyg/ANOXX_roster.htm")

        team = TeamDAO().getTeamByCode("NYJ")
        if team == None:
            TeamDAO().createTeam("New York Jets", "NYJ", "New York", "Jets", "teams/nyj/ANOXX_roster.htm")

        team = TeamDAO().getTeamByCode("KAN")
        if team == None:
            TeamDAO().createTeam("Kansas City Chiefs", "KAN", "Kansas City", "Chiefs", "teams/kan/ANOXX_roster.htm")

        team = TeamDAO().getTeamByCode("JAX")
        if team == None:
            TeamDAO().createTeam("Jacksonville Jaguars", "JAX", "Jacksonville", "Jaguars", "teams/jax/ANOXX_roster.htm")

        team = TeamDAO().getTeamByCode("MIA")
        if team == None:
            TeamDAO().createTeam("Miami Dolphins", "MIA", "Miami", "Dolphins", "teams/mia/ANOXX_roster.htm")

        team = TeamDAO().getTeamByCode("BAL")
        if team == None:
            TeamDAO().createTeam("Baltimore Ravens", "BAL;RAV", "Baltimore", "Ravens", "teams/rav/ANOXX_roster.htm")

        team = TeamDAO().getTeamByCode("ATL")
        if team == None:
            TeamDAO().createTeam("Atlanta Falcons", "ATL", "Atlanta", "Falcons", "teams/atl/ANOXX_roster.htm")

        team = TeamDAO().getTeamByCode("MIN")
        if team == None:
            TeamDAO().createTeam("Minnesota Vikings", "MIN", "Minnesota", "Vikings", "teams/min/ANOXX_roster.htm")

        team = TeamDAO().getTeamByCode("PIT")
        if team == None:
            TeamDAO().createTeam("Pittsburgh Steelers", "PIT", "Pittsburgh", "Steelers", "teams/pit/ANOXX_roster.htm")

        team = TeamDAO().getTeamByCode("BUF")
        if team == None:
            TeamDAO().createTeam("Buffalo Bills", "BUF", "Buffalo", "Bills", "teams/buf/ANOXX_roster.htm")

        team = TeamDAO().getTeamByCode("WAS")
        if team == None:
            TeamDAO().createTeam("Washington Redskins", "WAS", "Washington", "Redskins", "teams/was/ANOXX_roster.htm")

        team = TeamDAO().getTeamByCode("PHI")
        if team == None:
            TeamDAO().createTeam("Philadelphia Eagles", "PHI", "Philadelphia", "Eagles", "teams/phi/ANOXX_roster.htm")

        team = TeamDAO().getTeamByCode("IND")
        if team == None:
            TeamDAO().createTeam("Indianapolis Colts", "IND;CLT", "Indianapolis", "Colts", "teams/clt/ANOXX_roster.htm")

        team = TeamDAO().getTeamByCode("LAC")
        if team == None:
            TeamDAO().createTeam("Los Angeles Chargers", "LAC;SDG", "Los Angeles", "Chargers", "teams/sdg/ANOXX_roster.htm")

        team = TeamDAO().getTeamByCode("SEA")
        if team == None:
            TeamDAO().createTeam("Seattle Seahawks", "SEA", "Seattle", "Seahawks", "teams/sea/ANOXX_roster.htm")

        team = TeamDAO().getTeamByCode("CIN")
        if team == None:
            TeamDAO().createTeam("Cincinnati Bengals", "CIN", "Cincinnati", "Bengals", "teams/cin/ANOXX_roster.htm")

        team = TeamDAO().getTeamByCode("TAM")
        if team == None:
            TeamDAO().createTeam("Tamba Bay Buccaneers", "TAM", "Tamba Bay", "Buccaneers", "teams/tam/ANOXX_roster.htm")

        team = TeamDAO().getTeamByCode("SFO")
        if team == None:
            TeamDAO().createTeam("San Francisco 49ers", "SFO", "San Francisco", "49ers", "teams/sfo/ANOXX_roster.htm")

        team = TeamDAO().getTeamByCode("HOU")
        if team == None:
            TeamDAO().createTeam("Houston Texans", "HOU;HTX", "Houston", "Texans", "teams/htx/ANOXX_roster.htm")

        team = TeamDAO().getTeamByCode("NOR")
        if team == None:
            TeamDAO().createTeam("New Orleans", "NOR", "New Orleans", "Saints", "teams/nor/ANOXX_roster.htm")

        team = TeamDAO().getTeamByCode("OAK")
        if team == None:
            TeamDAO().createTeam("Oakland Raiders", "OAK;RAI", "Oakland", "Raiders", "teams/rai/ANOXX_roster.htm")

        team = TeamDAO().getTeamByCode("DEN")
        if team == None:
            TeamDAO().createTeam("Denver Broncos", "DEN", "Denver", "Broncos", "teams/den/ANOXX_roster.htm")
