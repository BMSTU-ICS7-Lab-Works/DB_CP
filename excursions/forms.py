from django import forms
from django.core.exceptions import ValidationError
from .BL import filltime
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

class scheduleSelectForm(forms.Form):
    Понедельник = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=filltime)
    Вторник = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=filltime)
    Среда = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=filltime)
    Четверг = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=filltime)
    Пятница = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=filltime)
    Суббота = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=filltime)
    Воскресенье = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=filltime)

