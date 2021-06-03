from django import forms
from django.core.exceptions import ValidationError
from .BL import filltime
from phonenumber_field.formfields import PhoneNumberField

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

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError('Цена экскурсии не может быть отрицательной!')
    name = forms.CharField(label='Название')
    description = forms.CharField(widget=forms.Textarea, label='Описание экскурсии')
    price = forms.IntegerField(label='Цена')
    guides = forms.ChoiceField(label='выберите гида')


class timeSelectForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.times = kwargs.pop('time')
        super(timeSelectForm, self).__init__(*args, **kwargs)
        schedule = []
        for i in range(len(self.times)):
            time = self.times[i]
            schedule.append((i+1, time.day + ' ' + time.time))

        self.fields['time'] = forms.ChoiceField(choices=schedule)
    time = forms.ChoiceField(label='время')

class scheduleSelectForm(forms.Form):
    Понедельник = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=filltime)
    Вторник = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=filltime)
    Среда = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=filltime)
    Четверг = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=filltime)
    Пятница = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=filltime)
    Суббота = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=filltime)
    Воскресенье = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=filltime)



class confirmationForm(forms.Form):
    name = forms.CharField(label='Имя')
    phone = PhoneNumberField(label='Номер телефона')

