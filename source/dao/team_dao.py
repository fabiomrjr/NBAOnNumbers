import resources.config as config
from sqlalchemy import create_engine, text, update
from sqlalchemy.orm import sessionmaker
from source.model.team import Team
from source.dao.dao import DAO

class TeamDAO(DAO):
    
    def __init__(self):
        DAO.__init__(self, config.connectionStringNBA)

    def createTeam(self, full_name, code, city, name, homepage, division, conference, league):
        dao = DAO(config.connectionStringNBA)
        #dao.startConnection()
        
        c1 = Team(full_name, code, city, name, homepage, division, conference, league)

        try:
            dao.session.add(c1)
            dao.session.commit()
        except:
            dao.session.rollback()
            raise
        dao.quitConnection()

        return c1

    def updateTeam(self, team_id, full_name, code, city_name, name, homepage, division, conference, league):
        dao = DAO(config.connectionStringNBA)
        #dao.startConnection()

        try:
            stmt = (update(Team).where(Team.id_team == team_id)
                    .values(full_name = full_name, code = code, city_name = city_name, name = name, homepage = homepage, division = division, conference = conference, league = league))
            dao.session.execute(stmt)
            dao.session.commit()
            item = dao.session.query(Team).filter(Team.id_team == team_id).first()
        except:
            dao.session.rollback()            
            raise
        dao.quitConnection()

        return item
    
    def getTeamByCode(self, code):
        dao = DAO(config.connectionStringNBA)
        #dao.startConnection()
        
        try:
            item = dao.session.query(Team).filter(Team.code.like("%" + code + "%")).first()
        except:
            dao.session.rollback()
            raise
        dao.quitConnection()
        return item
    
    def getTeamByFullName(self, fullname):
        dao = DAO(config.connectionStringNBA)
        #dao.startConnection()
        
        try:
            item = dao.session.query(Team).filter(Team.full_name.like("%" + fullname + "%")).first()
        except:
            dao.session.rollback()
            raise
        dao.quitConnection()
        return item
                            
    def createOrUpdateTeams(self, full_name, code, city_name, name, homepage, division, conference, league):
        team = self.getTeamByFullName(full_name)
        
        if team != None:
            return self.updateTeam(team.id_team, full_name, code, city_name, name, homepage, division, conference, league)
        
        return self.createTeam(full_name, code, city_name, name, homepage, division, conference, league)
    
    def listTeams(self):
        dao = DAO(config.connectionStringNBA)
        #dao.startConnection()
        
        try:
            item = dao.session.query(Team).all()
        except:
            dao.session.rollback()
            raise
        dao.quitConnection()
        
        return item