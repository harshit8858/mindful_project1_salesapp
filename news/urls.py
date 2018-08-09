from django.conf.urls import url
from .views import *


urlpatterns = [
    # url(r'^$', news, name='news'),
    url(r'^news_list/', news, name='news'),
    url(r'^add_news/', news_add, name="news_add"),
    # id,slug based url below this
    url(r'^(?P<slug>[\w-]+)/$', news_details, name='news_details'),
    url(r'^(?P<slug>[\w-]+)/edit/', news_edit, name='news_edit'),
    url(r'^(?P<slug>[\w-]+)/delete/', news_delete, name='news_delete'),
]
