from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    


from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class PasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User 


