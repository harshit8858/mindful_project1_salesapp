from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^payment/', payment, name="payment"),
    url(r'^add_payment/', payment_add, name='payment_add'),
    url(r'^(\d+)/$', payment_details, name='payment_details'),
    url(r'^(\d+)/edit/', payment_edit, name='payment_edit'),
    url(r'^(\d+)/delete/', payment_delete, name='payment_delete'),
]
