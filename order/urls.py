from django.urls import path, include
from order import views
from order.views import confirm_order

# from order.views import show_order

urlpatterns = [
    path('', views.SushiList.as_view(), name='home'),
    path('order/', views.OrderList.as_view(), name='order'),
    path('inari/', views.inari, name='inari'),
    path('maki/', views.maki, name='maki'),
    path('nigiri/', views.nigiri, name='nigiri',),
    path('topping/', views.topping, name='topping'),
    path('soup/', views.soup, name='soup'),
    path('side_dish/', views.side_dish, name='side_dish'),
    path('confirm/', views.confirm, name='confirm'),
    path('confirm_order/', views.confirm_order, name='confirm_order')
]
