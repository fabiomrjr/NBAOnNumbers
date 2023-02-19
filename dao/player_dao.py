import config
from sqlalchemy import create_engine, text, and_, update
from sqlalchemy.orm import sessionmaker
from model.player import Player
from dao.dao import DAO

class PlayerDAO():

    def __init__(self):
        pass
        #DAO.__init__(self)

    def createPlayer(name, position, number, player_nba_link):
        dao = DAO()
        dao.startConnection()
        c1 = Player(name, position, number, player_nba_link)

        try:
            dao.session.add(c1)
            dao.session.commit()
        except:
            dao.session.rollback()
            raise
        dao.quitConnection()
        return c1
    
    def updatePlayer(id_player, position, number, playerLink):
        dao = DAO()
        dao.startConnection()
        
        try:
            stmt = (update(Player).where(Player.id_player == id_player)
                    .values(position = position, number = number,
                            player_nba_link = playerLink))
            dao.session.execute(stmt)

            dao.session.commit()
            item = dao.session.query(Player).filter(Player.id_player == id_player).first()
        
        except:
            dao.session.rollback()
            raise
        dao.quitConnection()
        return item

    def getPlayerByName(name):
        dao = DAO()
        dao.startConnection()
        
        try:
            #stringText = "SELECT * FROM player where name = '" + str(name) + "' and number = '" + str(number) + "'"
            item = dao.session.query(Player).filter(and_(Player.name == str(name))).first()
        except:
            dao.session.rollback()
            raise
        dao.quitConnection()
        return item