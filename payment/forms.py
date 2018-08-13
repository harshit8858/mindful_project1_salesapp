from django import forms
from .models import *


PAYMENT_TYPE = (
    ('cash', 'CASH'),
    ('cheque', 'CHEQUE'),
    ('other', 'OTHER'),
)

class PaymentForm(forms.ModelForm):
    payment_type = forms.ChoiceField(choices=PAYMENT_TYPE, required=True, widget=forms.Select(attrs={'class':'dropdown-item', 'style':'width:200px'}))

    class Meta:
        model = Payment
        fields = [
            'customer',
            'amount',
            'description',
            'payment_type',
        ]
