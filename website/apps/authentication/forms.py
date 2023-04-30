from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    name = forms.CharField(label='name', widget=forms.TextInput(attrs={'class': 'from-input'}))
    email = forms.EmailField(label='email')
    password = forms.CharField(label='password', widget=forms.TextInput(attrs={'class': 'from-input'}))

    class Temp:
        model = User
        fields = ('name', 'email', 'password')


class LoginForm(forms.Form):
    email = forms.EmailField(label='email')
    password = forms.CharField(label='password', widget=forms.TextInput(attrs={'class': 'from-input'}))

    class Temp:
        model = User
        fields = ('email', 'password')
