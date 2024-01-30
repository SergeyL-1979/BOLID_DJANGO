from django import forms
from .models import Plist


# class PListSearchForm(forms.Form):
#     name = forms.CharField(required=False, label='Name')
#     firstname = forms.CharField(required=False, label='First Name')
#     midname = forms.CharField(required=False, label='Middle Name')
#     workphone = forms.CharField(required=False, label='Work Phone')
#     homephone = forms.CharField(required=False, label='Home Phone')
#     tabnumber = forms.CharField(required=False, label='Tab Number')


class PlistForm(forms.ModelForm):
    class Meta:
        model = Plist
        fields = ['name', 'firstname', 'midname', 'workphone', 'homephone', 'company', 'post', 'tabnumber', ]

    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите фамилию'}),
        'firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}),
        'midname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите отчество'}),
        'workphone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите рабочий телефон'}),
        'homephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите домашний телефон'}),
        'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите компанию'}),
        'post': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите должность'}),
        'tabnumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите табельный номер'}),
    }


class SearchForm(forms.Form):
    employee_name = forms.CharField(label='Имя сотрудника', max_length=100)
    min_date = forms.DateInput()
    max_date = forms.DateInput()
