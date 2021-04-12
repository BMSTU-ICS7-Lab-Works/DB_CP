from django import forms

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

class createGuideForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    patronymic = forms.CharField()
    qualification = forms.CharField()
    biography = forms.CharField()
    experience = forms.IntegerField
