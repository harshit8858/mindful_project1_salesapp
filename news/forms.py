from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelChoiceField
from .models import *


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = [
            'date',
            'title',
            'body',
        ]
