import resources.config as config
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

class DAO:

    engine = None
    session = None
    
    def __init__(self, url):
        if self.session == None:
            self.engine = create_engine(config.connectionStringNBA)
            Session = sessionmaker(bind=self.engine)
            self.session = Session()
            self.session.expire_on_commit = False

    def __del__(self):
        if self.session != None:
            self.session.close()
        
    def startConnection(self):
        if self.session == None:
            self.engine = create_engine(config.connectionStringNBA)
            Session = sessionmaker(bind=self.engine)
            self.session = Session()
            self.session.expire_on_commit = False
    
    def quitConnection(self):
        if self.session != None:
            self.session.close()
