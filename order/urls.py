from django.urls import path, include
from .models import views

urlpatterns = [
    path('', views.SushiList.as_view(), name='home'),
]
