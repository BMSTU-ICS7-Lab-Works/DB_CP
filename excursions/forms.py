from django import forms
from django.core.exceptions import ValidationError
import datetime

class createExcursionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.guides = kwargs.pop('guides')
        super(createExcursionForm, self).__init__(*args, **kwargs)
        names = []
        for i in range(len(self.guides)):
            guide = self.guides[i]
            names.append((i+1, guide.first_name + ' ' + guide.last_name + ' ' + guide.patronymic))

        self.fields['guides'] = forms.ChoiceField(choices=names)

    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    price = forms.IntegerField()
    guides = forms.ChoiceField()


class createSightForm(forms.Form):
    name = forms.CharField()
    build_date = forms.DateField()
    type = forms.CharField()
    author = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)

    def clean_build_date(self):
        date = self.cleaned_data['build_date']
        if date > datetime.date.today():
            raise forms.ValidationError('Invalid build date')

class createGuideForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    patronymic = forms.CharField()
    qualification = forms.CharField()
    biography = forms.CharField(widget=forms.Textarea)
    experience = forms.IntegerField
