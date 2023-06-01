from .models import WhiteList
from django.forms import ModelForm, TextInput


class WhiteListForm(ModelForm):
    class Meta:
        model = WhiteList
        fields = ['car_number', 'name']

        widgets = {
            'car_number': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер автомобиля'
            }),
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя сотрудника'
            })
        }