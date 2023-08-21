from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Ramen, Sushi, Drink, Order
from django.views import generic
from django.views.generic.base import TemplateView
from django.contrib import admin


from .forms import BookTimeForm
# Create your views here.


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

    context: {
        "order": order
    }
    return render(request, "order.html", context=context)
