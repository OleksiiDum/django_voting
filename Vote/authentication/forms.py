from django import forms
from django.core.validators import validate_email
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser


class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    email_field = forms.EmailField(label="email", required=True, validators=[validate_email])
    password_field = forms.CharField(label="password", max_length=32, widget=forms.PasswordInput)
    