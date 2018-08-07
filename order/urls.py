from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^new_order/', new_order, name='new_order'),
    url(r'^all_order/', all_order, name='all_order'),
    url(r'^(\d+)/', order_details, name='order_details'),
]
