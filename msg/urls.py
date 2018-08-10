from django.conf.urls import url
from .views import *


urlpatterns = [
    # url(r'^$', msg, name='msg'),
    url(r'^msg_list/', msg, name='msg'),
    url(r'^add_msg/', msg_add, name="msg_add"),
    # id,slug based url below this
    url(r'^(?P<slug>[\w-]+)/$', msg_details, name='msg_details'),
    url(r'^(?P<slug>[\w-]+)/edit/', msg_edit, name='msg_edit'),
    url(r'^(?P<slug>[\w-]+)/delete/', msg_delete, name='msg_delete'),
]
