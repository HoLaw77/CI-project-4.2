from django.urls import path, include
from order import views

urlpatterns = [
    path('', views.SushiList.as_view(), name='home'),
    path('order/', views.OrderList.as_view(), name='order'),

]
