from django.shortcuts import render
from .models import Ramen, Sushi, Drink, Order
from django.views import generic
# Create your views here.


def food_order(request):
