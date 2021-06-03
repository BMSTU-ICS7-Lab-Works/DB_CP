from django import forms
from .BL import *


class LoginForm(forms.Form):
    username = forms.CharField(label='Никнейм')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')

    def clean_password(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not check_user_login(username, password, 3):
            raise forms.ValidationError('Неверное имя пользователя или пароль!')


class RegistrateForm(forms.Form):
    username = forms.CharField(label='Никнейм')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    repeat_password = forms.CharField(widget=forms.PasswordInput, label='Повторно введите пароль')

    def clean_username(self):
        username = self.cleaned_data['username']
        if find_user(username, 3):
            raise forms.ValidationError('Пользователь с таким именем уже существует!')

    def clean_repeat_password(self):
        password = self.cleaned_data['password']
        if password != self.cleaned_data['repeat_password']:
            raise forms.ValidationError('Пароль и повторенный пароль не совпадают!')
