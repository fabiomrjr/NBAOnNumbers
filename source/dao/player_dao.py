import resources.config as config
from sqlalchemy import create_engine, text, and_, update
from sqlalchemy.orm import sessionmaker
from source.model.player import Player
from source.dao.dao import DAO

class PlayerDAO(DAO):

    def __init__(self):
        pass
        DAO.__init__(self, config.connectionStringNBA)

    def createPlayer(self, name, position, number, player_nba_link):
        #dao = DAO()
        #dao.startConnection()
        c1 = Player(name, position, number, player_nba_link)

        try:
            self.session.add(c1)
            self.session.commit()
        except:
            self.session.rollback()
            raise
        #self.quitConnection()
        return c1
    
    def updatePlayer(id_player, position, number, playerLink):
        #dao = DAO()
        #dao.startConnection()
        
        try:
            stmt = (update(Player).where(Player.id_player == id_player)
                    .values(position = position, number = number,
                            player_nba_link = playerLink))
            self.session.execute(stmt)

            self.session.commit()
            item = self.session.query(Player).filter(Player.id_player == id_player).first()
        
        except:
            self.session.rollback()
            raise
        #dao.quitConnection()
        return item

    def getPlayerByName(self, name):
        #dao = DAO()
        #dao.startConnection()
        
        try:
            item = self.session.query(Player).filter(and_(Player.name == str(name))).first()
        except:
            self.session.rollback()
            raise
        #dao.quitConnection()
        return item
    
    def providePlayer(self, name, position, number, player_nba_link):
        playerSelected = self.getPlayerByName(name)
        
        if playerSelected == None:
            return self.createPlayer(name, position, number, player_nba_link)
        
        return playerSelected