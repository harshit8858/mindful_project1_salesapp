from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelChoiceField
from .models import *


USER_TYPE = (
    ('salesmanager','SALES-MANAGER'),
    ('salesmen','SALESMEN'),
)

s_admin = Profile.objects.filter(user_type='salesadmin')
s_manager = Profile.objects.filter(user_type='salesmanager')

class SignUpForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=USER_TYPE, required=True, widget=forms.Select(attrs={'class':'dropdown-item', 'style':'width:200px'}))
    sale_admin = ModelChoiceField(queryset=s_admin, required=False)
    sale_manager = ModelChoiceField(queryset=s_manager, required=False)

    class Meta:
        model = User
        fields = (
            'username',
            'user_type',
            'sale_admin',
            'sale_manager',
            'password1',
            'password2',
        )



class CustomerForm(forms.ModelForm):
    sale_manager = ModelChoiceField(queryset=s_manager, required=True)

    class Meta:
        model = Customer
        fields = (
            'name',
            'sale_manager',
            'address',
            'mobile',
        )