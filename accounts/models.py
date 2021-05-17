from django.db import models

from sqlalchemy import event
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, DATE, ForeignKey, create_engine, Table
from sqlalchemy.ext.declarative import declarative_base
import os
import hashlib

admin_engine = create_engine("postgresql+psycopg2://postgres:1@localhost/Excursions")
Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    nickname = Column(String)
    password = Column(String)
    salt = Column(String)
    role = Column(Integer)

    def __init__(self, nickname, password, salt, role):
        self.nickname = nickname
        self.password = password
        self.salt = salt
        self.role = role

    def __repr__(self):
        return "<Users('%s', '%s', '%s', '%s')>" % (self.nickname, self.password, self.salt, self.role)


if __name__ == '__main__':
    Base.metadata.create_all(admin_engine)
    Session = sessionmaker(bind=admin_engine)
    session = Session()

    salt = os.urandom(32)  # Запомните
    password = 'gbgtnrf1'
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000)
    admin_user = Users('admin', key.hex(), salt.hex(), 2)
    session.add(admin_user)
    session.commit()
