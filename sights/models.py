from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DATE, ForeignKey, create_engine, Table
from excursions.models import Base

admin_engine = create_engine("postgresql+psycopg2://postgres:1@localhost/Excursions")




