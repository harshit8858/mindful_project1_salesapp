from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(('main.urls', 'main'), namespace="main")),
    url(r'^product/', include(('product.urls', 'product'), namespace="product")),
    url(r'^order/', include(('order.urls', 'order'), namespace="order")),
]
