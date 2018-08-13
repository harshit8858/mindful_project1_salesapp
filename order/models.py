from django.db import models
from product.models import *
from main.models1 import *


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True, blank=True, null=True)
    remark = models.CharField(max_length=1000, blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    discount = models.PositiveIntegerField(blank=True, null=True)
    tax = models.PositiveIntegerField(blank=True, null=True)
    total = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.product)
