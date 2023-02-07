import config
from sqlalchemy import create_engine, text, and_
from sqlalchemy.orm import sessionmaker
from ..model.player import Player
from ..dao.dao import DAO

class PlayerDAO(DAO):

    def __init__(self):
        DAO.__init__(self)

    def createPlayer(self, name, position, number, status, active):

        c1 = Player(name, position, number, status, active)

        try:
            self.session.add(c1)
            self.session.commit()
        except:
            self.session.rollback()
            raise
        return c1

    def getPlayerByNameAndNumber(self, number, name):
        try:
            #stringText = "SELECT * FROM player where name = '" + str(name) + "' and number = '" + str(number) + "'"
            item = self.session.query(Player).filter(and_(Player.name == str(name), Player.number == str(number))).first()
        except:
            self.session.rollback()
            raise

        return item