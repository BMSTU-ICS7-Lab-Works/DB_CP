from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DATE, ForeignKey, create_engine, Table
from excursions.models import SightsExcursions
from excursions.models import Base

admin_engine = create_engine("postgresql+psycopg2://postgres:1@localhost/Excursions")

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
