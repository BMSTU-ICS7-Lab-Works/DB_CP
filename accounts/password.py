import hashlib
import os
from DB_CP.session_manager import Session_Manager
from .models import Users

def get_hashed_password(password, salt=None):
    if salt is None:
        salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        100000
    )
    return key, salt

def find_user(username):
    session_manager = Session_Manager()
    session_manager.setRole(0)
    session = session_manager.getSession()

    founded = session.query(Users).filter(Users.nickname == username).first()
    session.close()
    if founded is None:
        return False
    else:
        return True


def check_user_login(username, password):
    session_manager = Session_Manager()
    session_manager.setRole(0)
    session = session_manager.getSession()
    founded = session.query(Users).filter(Users.nickname == username).first()
    session.close()
    if founded is None:
        return False
    password_to_check = password
    salt = bytes.fromhex(founded.salt)
    key, salt = get_hashed_password(password_to_check, salt)
    if key.hex() == founded.password:
        return True
    else:
        return False

def get_role(username):
    session_manager = Session_Manager()
    session_manager.setRole(0)
    session = session_manager.getSession()
    founded = session.query(Users).filter(Users.nickname == username).first()
    session.close()
    return founded.role

def addUser(username, password):
    key, salt = get_hashed_password(password)
    session_manager = Session_Manager()
    session_manager.setRole(0)
    session = session_manager.getSession()

    user = Users(username, key.hex(), salt.hex(), 1)

    session.add(user)
    session.commit()
    session.close()