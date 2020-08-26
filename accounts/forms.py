from django import forms
from django.forms import ValidationError
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
# from .models import profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', ]

    def email_check(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            return True
        return False
