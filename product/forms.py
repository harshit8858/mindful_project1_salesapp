from django import forms
from .models import *
from .models1 import *
from .models2 import *


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'category',
        ]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'category',
            'name',
            'price',
            'image',
            'status',
        ]


class PriceCategoryForm(forms.ModelForm):
    class Meta:
        model = PriceCategory
        fields = [
            'price',
        ]