from sqlalchemy import Column, Integer, String, create_engine
from excursions.models import Base

admin_engine = create_engine("postgresql+psycopg2://postgres:1@localhost/Excursions")


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
