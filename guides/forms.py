from django import forms

class createGuideForm(forms.Form):
    def clean_experience(self):
        experience = self.cleaned_data['experience']
        if experience < 0:
            raise forms.ValidationError('Опыт работы не может быть отрицательным!')
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    patronymic = forms.CharField(label='Отчество')
    qualification = forms.CharField(label='Квалификация')
    biography = forms.CharField(widget=forms.Textarea, label='Биография')
    experience = forms.IntegerField(label='Опыт работы')



