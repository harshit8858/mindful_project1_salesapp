from django.conf.urls import url
from .views import *


urlpatterns = [
    # url(r'^$', message, name='message'),
    url(r'^messages_list/', messages, name='messages'),
    url(r'^add_message/', message_add, name="message_add"),
    # id,slug based url below this
    url(r'^(?P<slug>[\w-]+)/$', message_details, name='message_details'),
    url(r'^(?P<slug>[\w-]+)/edit/', message_edit, name='message_edit'),
    url(r'^(?P<slug>[\w-]+)/delete/', message_delete, name='message_delete'),
]
