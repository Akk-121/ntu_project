from .models import  CustomUser
from django import forms
from django.forms import ModelForm, TextInput, FileInput, EmailInput, PasswordInput, Textarea, Select
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import SetPasswordForm, AuthenticationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')