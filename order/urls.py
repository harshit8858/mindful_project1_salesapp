from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^add_to_cart/(\d+)/', add_to_cart, name='add_to_cart'),
    url(r'^remove_to_cart/(?P<slug>[\w-]+)/', remove_from_cart, name='remove_to_cart'),
    url(r'^cart/', get_cart, name='cart'),

]