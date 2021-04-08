import hashlib
import os

from django.http import HttpResponse
from django.shortcuts import render, redirect
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
# Create your views here.
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists
from .models import Users

from .forms import LoginForm, RegistrateForm


def login(request):
    if request.method == 'POST':
        admin_engine = create_engine("postgresql+psycopg2://postgres:1@localhost/Excursions")
        Base = declarative_base()
        Base.metadata.create_all(admin_engine)
        Session = sessionmaker(bind=admin_engine)
        session = Session()

        founded = session.query(Users).filter(Users.nickname == request.POST.get('username')).first()
        session.close()
        password_to_check = request.POST.get('password')
        salt = bytes.fromhex(founded.salt)
        new_key = hashlib.pbkdf2_hmac(
            'sha256',
            password_to_check.encode('utf-8'),
            salt,
            100000
        )
        if new_key.hex() == founded.password:
            request.session['role'] = founded.role
            return redirect('/home')
        else:
            return HttpResponse('Durashka')

    else:
        form = LoginForm()
    return render(request, '../templates/registration/login.html', {'form': form})


def logout(request):
    request.session['role'] = 0
    return redirect('/home')

def registration(request):
    if request.method == 'POST':
        if request.POST.get('username') == 'chacha':
            return HttpResponse('takoy chel uje est paka')
        else:
            #tut potencialno v otdelnu funksu nado
            if request.POST.get('password') == request.POST.get('repeat_password'):
                salt = os.urandom(32)
                password = request.POST.get('password')

                key = hashlib.pbkdf2_hmac(
                    'sha256',
                    password.encode('utf-8'),
                    salt,
                    100000)

                #tut zanosim v bd i govorim chto vse klass
                #registratia uspeh i domou
                return redirect('/home')
            else:
                HttpResponse('tut nado AJAX shob pisalo nepralno i povtoryalo')

        return redirect('/home')
    else:
        form = RegistrateForm()
        return render(request, '../templates/registration/registration.html', {'form': form})

