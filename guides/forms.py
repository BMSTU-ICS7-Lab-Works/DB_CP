from django import forms

class createGuideForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    patronymic = forms.CharField()
    qualification = forms.CharField()
    biography = forms.CharField(widget=forms.Textarea)
    experience = forms.IntegerField()



