from sqlalchemy import Column, Integer, String, create_engine
from excursions.models import Base

admin_engine = create_engine("postgresql+psycopg2://postgres:1@localhost/Excursions")


