from django.db import models
from main.models1 import *


PAYMENT_TYPE = (
    ('cash', 'CASH'),
    ('cheque', 'CHEQUE'),
    ('other', 'OTHER'),
)

class Payment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    amount = models.PositiveIntegerField()
    description = models.TextField()
    payment_type = models.CharField(max_length=100, choices=PAYMENT_TYPE, default='cash')
    remark = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.customer)
