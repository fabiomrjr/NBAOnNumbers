import pandas as pd
from datetime import datetime as dt

from ..dao.player_dao import PlayerDAO
from ..dao.player_property_dao import PlayerPropertyDAO

position_field = 3
player_name_field = 1
player_number_field = 0

class PlayerBuilder:
    def __init__(self):
     pass

    def check(self, table_roster_df, Team, baseYear):
        players = PlayerPropertyDAO().listAllPlayerOfTeam(Team.id_team)
        for contractedPlayers in players:
            contractedPlayers.date_fire = dt(int(baseYear), 6, 1, 9, 0, 0, 0)
            contractedPlayers.active = False

        for i in range(0, len(table_roster_df)):

            player_name = table_roster_df.values[i][player_name_field].replace("*","").replace("+","")
            if not pd.isna(table_roster_df.values[i][player_number_field]):
                player_number = int(table_roster_df.values[i][player_number_field])
            else:
                player_number = None

            if not pd.isna(table_roster_df.values[i][position_field]):
                player_position = table_roster_df.values[i][position_field].upper()
            else:
                player_position = None

            if player_name == "Player" or player_name == "Team Total":
                continue

            player = PlayerDAO().getPlayerByNameAndNumber(player_number, player_name)
            if player == None:
                player = PlayerDAO().createPlayer(player_name, player_position, player_number, "A", True)

            newPlayer = True
            for playerOld in players:
                if playerOld.player.name == player_name:
                    playerOld.active = True
                    playerOld.date_fire = None
                    newPlayer = False
                    break

            if newPlayer == True:
                hiring_date = dt(int(baseYear), 5, 1, 9, 0, 0, 0)
                PlayerPropertyDAO().createPlayerProperty(Team.id_team, player.id_player, hiring_date, None, True)

        PlayerPropertyDAO().commit(players)
        #PlayerDAO().closeSession()
        #PlayerPropertyDAO().closeSession()