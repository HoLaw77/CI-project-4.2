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

    def get_sushi(request):
        sushi = SUSHI.objects.all()
        print(sushi)
        return render(request, "order.html", {"sushi": sushi})


class OrderList(generic.ListView):
    model = Order
    template_name = "order.html"
    paginated_by = 1

    def get_form(request):
        if request.method == "POST":
            form = BookTimeForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("Your order has been confirmed.")
        else:
            form = BookTimeForm()

        return render(request, "order.html", {"form": form})
