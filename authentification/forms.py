from django import forms
from django.contrib.auth.forms import AuthenticationForm

class AuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Nom d\'utilisateur', max_length=254, widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label='Mot de Passe', widget=forms.PasswordInput(attrs={'autofocus': True, 'class': 'form-control'}))