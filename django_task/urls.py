from django.contrib import admin
from django.urls import path, include
from order.views import Order


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('order.urls'), name='order-urls'),
    path("account/", include("allauth.urls")),
]
