from django import forms
from django.core.exceptions import ValidationError
import datetime

class createExcursionForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    #уффф тут нужно гида получать id по имени и только потом добавлять
    guide_name = forms.CharField()
    guide_surname = forms.CharField()
    guide_patronymic = forms.CharField()
    price = forms.IntegerField()

class createSightForm(forms.Form):
    name = forms.CharField()
    build_date = forms.DateField()
    type = forms.CharField()
    author = forms.CharField()
    description = forms.CharField()

    def clean_build_date(self):
        #tut cheta shamanit'
        data = self.cleaned_data['build_date']

        if data > datetime.date.today():
            raise ValidationError('Invalid build date')

class createGuideForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    patronymic = forms.CharField()
    qualification = forms.CharField()
    biography = forms.CharField()
    experience = forms.IntegerField
