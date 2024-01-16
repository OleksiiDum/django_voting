from django import forms
from django.core.validators import validate_email


class RegisterForm(forms.Form):
    email_field = forms.EmailField(label="your email", required=True, validators=[validate_email])
    password_field = forms.CharField(label="your password", max_length=32, widget=forms.PasswordInput)
    confirm_password_field = forms.CharField(label="confirm password", max_length=32, widget=forms.PasswordInput)
    your_name = forms.CharField(label="your name", max_length=100)

class LoginForm(forms.Form):
    email_field = forms.EmailField(label="email", required=True, validators=[validate_email])
    password_field = forms.CharField(label="password", max_length=32, widget=forms.PasswordInput)
    