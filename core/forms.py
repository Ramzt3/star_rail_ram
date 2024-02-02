from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Character
from django import forms
from django.forms import ModelForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'username',
        'class': 'w3-input w3-round',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'password',
        'class': 'w3-input w3-round',
    }))


class AddCharacterForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'name',
        'class': 'w3-input w3-round',
    }))
    gender = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'gender',
        'class': 'w3-input w3-round',
    }))
    rarity = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'rarity',
        'class': 'w3-input w3-round',
    }))

    class Meta:
        model = Character
        fields = ["name", "gender", "rarity", "path", "element"] 
