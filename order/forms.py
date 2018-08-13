from django import forms
from .models import *

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = [
            'customer',
            'remark',
            'product',
            'quantity',
            'price',
            'discount',
            'tax',
            'total',
        ]
