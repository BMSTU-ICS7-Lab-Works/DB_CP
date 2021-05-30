import hashlib
import os
from excursions.models import Users
from.account_repositories import UsersRepository


class Roles:
    def __init__(self, rolenum, name):
        self.rolenum = rolenum
        self.name = name


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


def find_user(username, role):
    userRep = UsersRepository(role)
    if userRep.findUserByName(username) is None:
        return False
    else:
        return True


def getUser(username, role):
    userRep = UsersRepository(role)
    return userRep.findUserByName(username)



def check_user_login(username, password, role):
    userRep = UsersRepository(role)
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
    userRep = UsersRepository(3)
    fuser = userRep.findUserByName(username)
    return fuser.role


def addUser(username, password, role):
    key, salt = get_hashed_password(password)
    userRep = UsersRepository(3)
    userRep.addUser(Users(username, key.hex(), salt.hex(), 1))

def updateUserRole(username, roleset, role):
    userRep = UsersRepository(role)
    userRep.changeRole(username, roleset)

def getAllUsers(role):
    userRep = UsersRepository(role)
    return userRep.findAllUsers()



