from django.forms import ModelForm, TextInput, PasswordInput
from django.contrib.auth.models import User


class UsersForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            'username': TextInput(attrs={
                'class': 'input100',
                'placeholder': 'Логин',
                'name': 'username'
            }),
            'password': PasswordInput(attrs={
                'class': 'input100',
                'placeholder': 'Пароль',
                'name': 'password'
            })
        }