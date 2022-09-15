from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from account.models import myUser


class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    class Meta:
        model = myUser
        fields = ("username", "password1", "password2", "first_name", "last_name","gender","age")