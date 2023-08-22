from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Ramen, Sushi, Drink, Order
from django.views import generic
from django.views.generic.base import TemplateView
from django.contrib import admin


from .forms import BookTimeForm
# Create your views here.


def inari(request):
    return render(request, 'sushi/inari_sushi.html')


def maki(request):
    return render(request, 'sushi/maki_sushi.html')


def nigiri(request):
    return render(request, 'sushi/nigiri_sushi.html')


def topping(request):
    return render(request, 'ramen/topping.html')


def soup(request):
    return render(request, 'ramen/soup.html')

def side_dish(request):
    return render(request, 'ramen/side_dish.html')


class SushiList(generic.ListView):
    model = Sushi
    template_name = "index.html"
    paginated_by = 3


class OrderDetail(generic.DetailView):
    model = Order

    template_name = "order.html"


class OrderList(generic.ListView):
    model = Order
    template_name = "order.html"
    paginated_by = 1


def show_order(request):
    order = Order.objects.all()

    context = {
        "order": order
    }
    print(order)
    return render(request, "order.html", context=context)
