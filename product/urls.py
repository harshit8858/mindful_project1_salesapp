from django.conf.urls import url
from .views import *

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^category/$', category, name="category"),
    url(r'^add_category/', add_category, name="add_category"),
    url(r'^product/', product, name="product"),
    url(r'^add_product/', add_product, name="add_product"),
    url(r'^(?P<slug>[\w-]+)/$', product_detail, name="product_details"),
    url(r'^(?P<slug>[\w-]+)/edit/', product_edit, name="product_edit"),
    url(r'^category/(?P<slug1>[\w-]+)/$', category_detail, name="category_details"),
    url(r'^category/(?P<slug1>[\w-]+)/edit/', category_edit, name="category_edit"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
