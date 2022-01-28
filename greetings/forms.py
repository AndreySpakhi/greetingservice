from .models import User
from django.forms import ModelForm, TextInput, EmailInput


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'user_email']
        widgets = {
            'first_name': TextInput(attrs={
                'size': 50,
                'placeholder': 'Ваше ім’я:'
            }),
            'last_name': TextInput(attrs={
                'size': 50,
                'placeholder': 'Ваше прізвище:'
            }),
            'user_email': EmailInput(attrs={
                'size': 50,
                'placeholder': 'Ваш email:'
            }),
        }
