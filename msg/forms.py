from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelChoiceField
from .models import *


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = [
            'user',
            'message',
        ]


class MessageUserForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = [
            'message',
        ]
