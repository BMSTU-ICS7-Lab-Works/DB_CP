from django import forms

class createExcursionForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    #уффф тут нужно гида получать id по имени и только потом добавлять
    guide = forms.CharField()
    price = forms.IntegerField()

class createSightForm(forms.Form):
    name = forms.CharField()
    build_date = forms.DateField()
    type = forms.CharField()
    author = forms.CharField()
    description = forms.CharField()
