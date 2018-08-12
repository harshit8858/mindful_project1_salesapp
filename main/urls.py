from django.conf.urls import url
from .views import *

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', login, name='login'),
    url(r'^home/', index, name='index'),
    url(r'^user/', user, name='user'),
    url(r'^signup/', signup, name='signup'),
    url(r'^auth_check/', auth_check, name='check'),
    url(r'^logout/', logout, name='logout'),
    url(r'^invalid/', invalid, name='invalid'),
    url(r'^customer/$', customer, name='customer'),
    url(r'^customer_list/', customer_list, name='customer_list'),
    url(r'^reports/', reports, name="reports"),
    url(r'^dashboard/', dashboard, name="dashboard"),
    url(r'^location_tracking/', location_tracking, name="location_tracking"),
    url(r'^payment/', payment, name="payment"),
    url(r'^company_profile/$', company_profile, name="company_profile"),
    url(r'^company_profile/add/', company_profile_add, name="company_profile_add"),
    #id,slug based url below this
    url(r'^(?P<slug>[\w-]+)/$', user_details, name='user_details'),
    url(r'^(?P<slug>[\w-]+)/edit/', edit_user, name='edit_user'),
    url(r'^(?P<slug>[\w-]+)/delete/', delete_user, name='delete_user'),
    url(r'^customer/(?P<slug1>[\w-]+)/$', customer_details, name='customer_details'),
    url(r'^customer/(?P<slug1>[\w-]+)/edit/', edit_customer, name='edit_customer'),
    url(r'^customer/(?P<slug1>[\w-]+)/delete/', delete_customer, name='delete_customer'),
    url(r'^company_profile_edit/(\d+)/', company_profile_edit, name="company_profile_edit"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

