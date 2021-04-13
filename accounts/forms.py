from django import forms
from .password import *


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrateForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    repeat_password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if find_user(username):
            raise forms.ValidationError('User with this name already exists!')

    def clean_repeat_password(self):
        password = self.cleaned_data['password']
        if password != self.cleaned_data['repeat_password']:
            raise forms.ValidationError('Password and Repeated password doesnt match!')