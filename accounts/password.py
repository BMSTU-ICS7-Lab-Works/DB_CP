import hashlib
import os
from .models import Users
from.account_repositories import UsersRepository

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
    userRep = UsersRepository(0)
    if userRep.findUserByName(username) is None:
        return False
    else:
        return True


def check_user_login(username, password):
    userRep = UsersRepository(0)
    fuser = userRep.findUserByName(username)
    if fuser is None:
        return False
    salt = bytes.fromhex(fuser.salt)
    key, salt = get_hashed_password(password, salt)
    if key.hex() == fuser.password:
        return True
    else:
        return False


def get_role(username):
    userRep = UsersRepository(0)
    fuser = userRep.findUserByName(username)
    return fuser.role


def addUser(username, password):
    key, salt = get_hashed_password(password)
    userRep = UsersRepository(0)
    userRep.addUser(Users(username, key.hex(), salt.hex(), 1))
