from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.SushiList.as_view(), name='home'),
    path('', views.OrderList.as_view(), name='order'),

]
