from django.urls import path, include
from order import views
from order.views import confirm_order

# from order.views import show_order

urlpatterns = [
    path('', views.SushiList.as_view(), name='home'),
    path('order/', views.OrderList.as_view(), name='order'),
    path('sushi/', views.sushi, name='sushi',),
    path('ramen/', views.ramen, name='ramen'),
    path('drink/', views.drink, name='drink'),
    path('confirm/', views.ConfirmList.as_view(), name='confirmlist'),
    path('confirm_order/', views.confirm_order, name='confirm_order'),
    path('sushi_order/', views.sushi_order, name='sushi_order'),
    path('ramen_order/', views.ramen_order, name='ramen_order'),
    path('drink_order/', views.drink_order, name='drink_order'),

]
