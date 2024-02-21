from django import forms
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from .models import Plist


# ==================================================================================================
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


# class PLogDataSearchForm(forms.Form):
#     min_datetime = forms.DateTimeField(
#         label='Начальная дата', required=False, input_formats=['%Y-%m-%d %H:%M:%S'])
#     max_datetime = forms.DateTimeField(
#         label='Конечная дата', required=False, input_formats=['%Y-%m-%d %H:%M:%S'])
#     hozorgan = forms.CharField(label='Фамилия', required=False)

