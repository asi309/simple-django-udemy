from django import forms
from django.core import validators
from django.forms import ModelForm
from pro2.models import User

class SignInForm(ModelForm):
    class Meta:
        model = User
        fields = ['fname', 'lname', 'email']