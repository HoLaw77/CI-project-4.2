from django.shortcuts import render
from django.views import generic
from order.models import Ramen, Sushi, Drink, Order

# Create your views here.


class InariSushiList(generic.ListView):
    model = Sushi
    template_name = "inari_sushi.html"
