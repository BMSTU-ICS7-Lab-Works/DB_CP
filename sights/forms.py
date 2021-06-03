import datetime

from django import forms

class createSightForm(forms.Form):
    name = forms.CharField(label='Название')
    build_date = forms.DateField(label='Дата постройки')
    type = forms.CharField(label='Тип достопримечательности')
    author = forms.CharField(label='Автор')
    description = forms.CharField(widget=forms.Textarea, label='Описание')

    def clean_build_date(self):
        date = self.cleaned_data['build_date']
        if date > datetime.date.today():
            raise forms.ValidationError('Дата постройки не может быть позднее текущей даты')