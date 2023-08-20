from django.urls import path, include
from order import views

urlpatterns = [
    path('', views.SushiList.as_view(), name='home'),
    path('order/', views.OrderList.as_view(), name='order'),
    path('order/<int:order_id>', views.OrderDetail.as_view(), name='order_detail'),
]
