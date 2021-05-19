from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DATE, ForeignKey, create_engine, Table
from sqlalchemy.ext.declarative import declarative_base

admin_engine = create_engine("postgresql+psycopg2://postgres:1@localhost/Excursions")
Base = declarative_base()


SightsExcursions = Table('SightsExcursions', Base.metadata,
    Column('sightsId', Integer,
      ForeignKey('sights.id', ondelete='cascade')),
    Column('excursionsId', Integer,
        ForeignKey('excursions.id', ondelete='cascade')))


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

