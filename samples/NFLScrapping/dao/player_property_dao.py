import config
from sqlalchemy import create_engine, text, and_
from sqlalchemy.orm import sessionmaker, subqueryload, selectinload
from ..model.player import Player
from ..model.team import Team
from ..model.player_property import PlayerProperty
from ..dao.dao import DAO

class PlayerPropertyDAO(DAO):

    def __init__(self):
        DAO.__init__(self)

    def commit(self, players):
        try:
            self.session.add_all(players)
            self.session.commit()
        except:
            self.session.rollback()
            raise

    def createPlayerProperty(self, team_id, player_id, date_hire, date_fire, isActive):

        c1 = PlayerProperty(team_id, player_id, date_hire, date_fire, isActive)

        try:
            self.session.add(c1)
            self.session.commit()
        except:
            self.session.rollback()
            raise
        return c1

    def getPlayerPropertyByPlayerNameAndTeamCode(self, team_code, player_name):
        try:
            #options(selectinload(Player.player), selectinload(Team.team))
            item = self.session.query(PlayerProperty).filter(and_(PlayerProperty.player.has(Player.name == player_name), PlayerProperty.team.has(Team.code.like("%"+ team_code + "%")))).first()
        except:
            self.session.rollback()
            raise

        return item

    def listAllPlayerOfTeam(self, team_id):
        try:
            item = self.session.query(PlayerProperty).options(selectinload(PlayerProperty.player)).filter(PlayerProperty.id_team == team_id).all()# from_statement(text(stringText)).all()
        except:
            self.session.rollback()
            raise

        return item