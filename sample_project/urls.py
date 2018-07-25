from django.contrib import admin
from django.conf.urls import url,include
from django.conf import settings

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^', include('user.urls')),
]


