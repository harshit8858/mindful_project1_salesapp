from django.conf.urls import url
from .views import *

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^category/', category, name="category"),
    url(r'^product/', product, name="product"),
    url(r'^(?P<slug>[\w-]+)/', product_detail, name="product_details"),
    url(r'^(?P<slug>[\w-]+)/edit/', product_edit, name="product_edit"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
