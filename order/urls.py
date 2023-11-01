from django.urls import path, include
from order import views
from order.views import confirm_order


 
urlpatterns = [
    path('', views.SushiList.as_view(), name='home'),
    path('order/', views.order, name='order'),
    path('sushi/', views.sushi, name='sushi',),
    path('ramen/', views.ramen, name='ramen'),
    path('drink/', views.drink, name='drink'),
    path('confirm_order/', views.confirm_order, name='confirm_order'),
    path('sushi_order/', views.sushi_order, name='sushi_order'),
    path('ramen_order/', views.ramen_order, name='ramen_order'),
    path('drink_order/', views.drink_order, name='drink_order'),
    path('delete_drink_order/<order_id>', views.delete_drink_order, name='delete_drink_order'),
    path('delete_ramen_order/<order_id>', views.delete_ramen_order, name='delete_ramen_order'),
    path('delete_sushi_order/<order_id>', views.delete_sushi_order, name='delete_sushi_order'),
    path('edit_drink_order/<order_id>', views.edit_drink_order, name='edit_drink_order'),
    path('edit_ramen_order/<order_id>', views.edit_ramen_order, name='edit_ramen_order'),
    path('edit_sushi_order/<order_id>', views.edit_sushi_order, name='edit_sushi_order'),
    
]