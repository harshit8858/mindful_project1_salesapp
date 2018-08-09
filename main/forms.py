from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelChoiceField
from .models import *
from .models1 import *


USER_TYPE = (
    ('salesmanager','SALES-MANAGER'),
    ('salesmen','SALESMEN'),
)

# s_admin = Profile.objects.filter(user_type='salesadmin')
s_manager = Profile.objects.filter(user_type='salesmanager')

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput())
    last_name = forms.CharField(required=True, widget=forms.TextInput())
    mobile = forms.IntegerField(required=True,widget=forms.NumberInput())
    user_type = forms.ChoiceField(choices=USER_TYPE, required=True, widget=forms.Select(attrs={'class':'dropdown-item', 'style':'width:200px'}))
    # sale_admin = ModelChoiceField(queryset=s_admin, required=False)
    sale_manager = ModelChoiceField(queryset=s_manager, required=False)

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'mobile',
            'user_type',
            # 'sale_admin',
            'sale_manager',
            'password1',
            'password2',
        )


class EditUserForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput())
    last_name = forms.CharField(required=True, widget=forms.TextInput())
    mobile = forms.IntegerField(required=True,widget=forms.NumberInput())
    user_type = forms.ChoiceField(choices=USER_TYPE, required=True, widget=forms.Select(attrs={'class':'dropdown-item', 'style':'width:200px'}))
    # sale_admin = ModelChoiceField(queryset=s_admin, required=False)
    sale_manager = ModelChoiceField(queryset=s_manager, required=False)

    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'mobile',
            'user_type',
            # 'sale_admin',
            'sale_manager',
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


class CompanyProfileEditForm(forms.ModelForm):

    class Meta:
        model = Company_Profile
        exclude = {

        }
