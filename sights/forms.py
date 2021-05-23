import datetime

from django import forms

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