from django.http import HttpResponse
from django.shortcuts import render
from .models import Ramen, Sushi, Drink, Order
from django.views import generic
from django.views.generic.base import TemplateView
# Create your views here.


class SushiList(generic.ListView):
    model = Sushi
    template_name = "index.html"
    paginated_by = 3


class OrderList(generic.ListView):
    model = Order
    template_name = "order.html"
    paginated_by = 1
