import config
from sqlalchemy import create_engine, text, and_
from sqlalchemy.orm import sessionmaker, subqueryload, selectinload
from ..model.game import Game
from ..dao.dao import DAO

class GameDAO(DAO):

    def __init__(self):
        DAO.__init__(self)

    def createGame(self, home_team_id, visit_team_id, startDateTime, home_score, visit_score, winner_team_id):

        c1 = Game(home_team_id, visit_team_id, startDateTime, home_score, visit_score, winner_team_id)

        try:
            self.session.add(c1)
            self.session.commit()
        except:
            self.session.rollback()
            raise
        return c1

    def getGameByTeamsAndDateTime(self, home_team_id, visit_team_id, startDateTime):
        try:
            #options(selectinload(Game.visit_team), selectinload(Game.home_team))
            item = self.session.query(Game).filter(and_(Game.id_home_team == home_team_id, Game.id_visit_team == visit_team_id, Game.date == startDateTime.strftime("%Y-%m-%d %H:%M:00"))).first()
        except:
            self.session.rollback()
            raise

        return item