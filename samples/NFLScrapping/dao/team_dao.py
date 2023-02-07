import config
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from ..model.team import Team
from ..dao.dao import DAO

class TeamDAO(DAO):
    def __init__(self):
        DAO.__init__(self)

    def createTeam(self, full_name, code, city, name, homepage):
        c1 = Team(full_name, code, city, name, homepage)

        try:
            self.session.add(c1)
            self.session.commit()
        except:
            self.session.rollback()
            raise
        return c1

    def getTeamByCode(self, code):
        try:
            item = self.session.query(Team).filter(Team.code.like("%" + code + "%")).first()
        except:
            self.session.rollback()
            raise

        return item

    def listTeamsWithHomePage(self):
        try:
            item = self.session.query(Team).filter(Team.homepage.isnot(None)).all()
        except:
            self.session.rollback()
            raise

        return item