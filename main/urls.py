from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', login, name='login'),
    url(r'^home/', index, name='index'),
    url(r'^user/', user, name='user'),
    url(r'^signup/', signup, name='signup'),
    url(r'^auth_check/', auth_check, name='check'),
    url(r'^logout/', logout, name='logout'),
    url(r'^invalid/', invalid, name='invalid'),
    url(r'^customer/', customer, name='customer'),
    url(r'^customer_list/', customer_list, name='customer_list'),
]
