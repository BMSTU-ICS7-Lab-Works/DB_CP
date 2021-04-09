from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Session_Manager():

    admin_engine = create_engine("postgresql+psycopg2://postgres:1@localhost/Excursions")
    unlogged_engine = create_engine("postgresql+psycopg2://postgres:1@localhost/Excursions")
    logged_engine = create_engine("postgresql+psycopg2://postgres:1@localhost/Excursions")



    def __init__(self):
        self.role = 0
        self.sessionmaker = sessionmaker(bind=self.unlogged_engine)
        self.sesssion = self.sessionmaker()

    def setRole(self, role):
        if 0 <= role <= 2:
            self.role = role
        else:
            raise Exception("Wrong role")

    def getSession(self):
        if self.role == 0:
            self.sessionmaker = sessionmaker(bind=self.admin_engine)
            self.sesssion = self.sessionmaker()
            return self.sesssion
        elif self.role == 1:
            self.sessionmaker = sessionmaker(bind=self.unlogged_engine)
            self.sesssion = self.sessionmaker()
            return self.sesssion
        elif self.role == 2:
            self.sessionmaker = sessionmaker(bind=self.logged_engine)
            self.sesssion = self.sessionmaker()
            return self.sesssion
        else:
            raise Exception("Wrong role")

