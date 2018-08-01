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
    url(r'^(?P<slug>[\w-]+)/$', user_details, name='user_details'),
    url(r'^(?P<slug>[\w-]+)/edit/', edit_user, name='edit_user'),
    url(r'^(?P<slug>[\w-]+)/delete/', delete_user, name='delete_user'),

]
