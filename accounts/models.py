
from sqlalchemy import create_engine
from excursions.models import Users
import os
import hashlib
from DB_CP.sessionmanager import SessionManager

admin_engine = create_engine("postgresql+psycopg2://postgres:1@localhost/Excursions")


if __name__ == '__main__':
    #Base.metadata.create_all(admin_engine)
    # Session = sessionmaker(bind=admin_engine)
    # session = Session()
    session_manager = SessionManager(3)
    session = session_manager.getSession()
    salt = os.urandom(32)  # Запомните
    password = 'gbgtnrf1'
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000)
    admin_user = Users('admin', key.hex(), salt.hex(), 3)
    session.add(admin_user)
    session.commit()
