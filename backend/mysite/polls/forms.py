from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *


class Sign_Up_Form(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "password1", "password2", "username"]


class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = "__all__"


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = "__all__"





