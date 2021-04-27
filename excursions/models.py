#from django.db import models

# Create your models here.

from sqlalchemy import event
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, DATE, ForeignKey, create_engine, Table
from sqlalchemy.ext.declarative import declarative_base

admin_engine = create_engine("postgresql+psycopg2://postgres:1@localhost/Excursions")
Base = declarative_base()



SightsExcursions = Table('SightsExcursions', Base.metadata,
    Column('sightsId', Integer,
      ForeignKey('sights.id', ondelete='cascade')),
    Column('excursionsId', Integer,
        ForeignKey('excursions.id', ondelete='cascade')))


class Sights(Base):
    __tablename__ = 'sights'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    build_date = Column(DATE)
    type = Column(String)
    author = Column(String)
    description = Column(String)
    excursion = relationship('Excursions', secondary=SightsExcursions, back_populates='sight')

    def __init__(self, name, build_date, type, author, description):
        self.name = name
        self.build_date = build_date
        self.type = type
        self.author = author
        self.description = description

    def __repr__(self):
        return "<Sights('%s', '%s', '%s', '%s', '%s')>" % (self.name, self.build_date, self.type,
                                                           self.author, self.description)


class Guides(Base):
    __tablename__ = 'guides'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    patronymic = Column(String)
    qualification = Column(String)
    biography = Column(String)
    experience = Column(Integer)

    def __init__(self, first_name, last_name, patronymic, qualification, biography, experience):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.qualification = qualification
        self.biography = biography
        self.experience = experience

    def __repr__(self):
        return "<Guide('%s', '%s', '%s', '%s', '%s', '%s')>" % (
        self.first_name, self.last_name, self.patronymic, self.qualification, self.biography, self.experience)


class Excursions(Base):
    __tablename__ = 'excursions'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    guide = Column(Integer, ForeignKey('guides.id'))
    price = Column(Integer)
    sight = relationship('Sights', secondary=SightsExcursions, back_populates='excursion')

    def __init__(self, name, description, guide, price):
        self.name = name
        self.description = description
        self.guide = guide
        self.price = price

    def __repr__(self):
        return "%s, %s, %s, %s" % (self.name, self.description, self.guide, self.price)

if __name__ == '__main__':
    Base.metadata.create_all(admin_engine)
    # Session = sessionmaker(bind=admin_engine)
    # session = Session()
    # vasiliSight = Sights('Храм Василия Блаженного', '02-10-1552', 'Шатровый храм', 'Постник Яковлев', 'православный '
    #                                                 'храм на Красной площади в Москве, памятник русской архитектуры.')
    # session.add(vasiliSight)
    # # ourSight = session.query(Sights).first()
    # # print(ourSight)
    # # print(vasiliSight.id)
    # session.commit()
    # #print(vasiliSight.id)
    # session.close()

