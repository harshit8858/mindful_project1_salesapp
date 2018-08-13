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

STATUS = (
    ('active','ACTIVE'),
    ('inactive','INACTIVE'),
)

# s_admin = Profile.objects.filter(user_type='salesadmin')
s_manager = Profile.objects.filter(user_type='salesmanager')

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput())
    last_name = forms.CharField(required=True, widget=forms.TextInput())
    address = forms.CharField(required=True, widget=forms.TextInput())
    state = forms.CharField(required=True, widget=forms.TextInput())
    city = forms.CharField(required=True, widget=forms.TextInput())
    country = forms.CharField(required=True, widget=forms.TextInput())
    pincode = forms.IntegerField(required=True,widget=forms.NumberInput())
    user_type = forms.ChoiceField(choices=USER_TYPE, required=True, widget=forms.Select(attrs={'class':'dropdown-item', 'style':'width:200px'}))
    # sale_admin = ModelChoiceField(queryset=s_admin, required=False)
    sale_manager = ModelChoiceField(queryset=s_manager, required=False)
    status = forms.ChoiceField(choices=STATUS, required=True, widget=forms.Select(attrs={'class':'dropdown-item', 'style':'width:200px'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput())
    profile_pic = forms.FileField()

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'profile_pic',
            'username',
            'status',
            'email',
            'address',
            'state',
            'pincode',
            'city',
            'country',
            'user_type',
            # 'sale_admin',
            'sale_manager',
            'password1',
            'password2',
        )


class EditUserForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput())
    last_name = forms.CharField(required=True, widget=forms.TextInput())
    address = forms.CharField(required=True, widget=forms.TextInput())
    state = forms.CharField(required=True, widget=forms.TextInput())
    city = forms.CharField(required=True, widget=forms.TextInput())
    country = forms.CharField(required=True, widget=forms.TextInput())
    pincode = forms.IntegerField(required=True,widget=forms.NumberInput())
    user_type = forms.ChoiceField(choices=USER_TYPE, required=True, widget=forms.Select(attrs={'class':'dropdown-item', 'style':'width:200px'}))
    # sale_admin = ModelChoiceField(queryset=s_admin, required=False)
    sale_manager = ModelChoiceField(queryset=s_manager, required=False)
    status = forms.ChoiceField(choices=STATUS, required=True, widget=forms.Select(attrs={'class':'dropdown-item', 'style':'width:200px'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput())
    profile_pic = forms.FileField()

    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'profile_pic',
            'status',
            'email',
            'address',
            'state',
            'pincode',
            'city',
            'country',
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
            'customer_code',
            'sale_manager',
            'status',
            'address',
            'pincode',
            'country',
            'city',
            'state',
            'area',
            'lattitude',
            'longitude',
            'email',
            'mobile',
        )


class CompanyProfileEditForm(forms.ModelForm):

    class Meta:
        model = Company_Profile
        exclude = {

        }
