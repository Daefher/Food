from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms



class AgregarForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]
        email = forms.EmailField(max_length=128, help_text='Opcional')