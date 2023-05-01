import resources.config as config
import pandas as pd
import math

from sqlalchemy import create_engine, text, and_, update
from sqlalchemy.orm import sessionmaker, subqueryload, selectinload
from model.game import Game as game
from dao.player_dao import PlayerDAO
from dao.team_dao import TeamDAO
from scrapers.nba_web_site.nba_team_info_scrap import NBATeamInfoScrap


class PlayersDBCreatorService():
    def __init__(self):
        pass
        #DAO.__init__(self)
        
    def listPlayersHome(self):
        teamsList = TeamDAO().listTeams()
        dfPlayers = pd.DataFrame()
        dfPlayersPartial = pd.DataFrame()
        
        for team in teamsList:
            dfPlayersPartial = NBATeamInfoScrap().getPlayers(config.nbaBaseURL + team.homepage)
            
            if not dfPlayersPartial.empty:
                for index, row in dfPlayersPartial.iterrows():
                    if not math.isnan(row['#']):
                        self.createOrUpdatePlayer(row['Player'], row['Pos'], row['#'], row['PlayerLink'])
                
                dfPlayers = pd.concat([dfPlayers, dfPlayersPartial])
        
        return dfPlayers
    
    def createOrUpdatePlayer(self, player_name, pos, number, player_link):
        player = PlayerDAO().getPlayerByName(player_name)

        if player != None:
            return PlayerDAO().updatePlayer(player.id_player, pos, number, player_link)
        
        return PlayerDAO().createPlayer(player_name, pos, number, player_link)
    