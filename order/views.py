from django.shortcuts import render
from .models import Ramen, Sushi, Drink, Order
# Create your views here.

def food_order(request):
    