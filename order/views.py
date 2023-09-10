from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Ramen, Sushi, Drink, Order, Confirm
from django.views import generic
from django.views.generic import TemplateView, DetailView
from django.contrib import admin


from .forms import BookTimeForm, SushiOrder
# Create your views here.

def sushi(request):
    return render(request, 'sushi/sushi.html')


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

class OrderList(generic.ListView):
    model = Order
    template_name = "order.html"
    paginated_by = 1



def confirm_order(request):
    if request.method == "POST":
        form = BookTimeForm(request.POST)
       
        if form.is_valid():
            form.save(commit = False)
            form.save()
          
        else:
            print('form invalid')

    form = BookTimeForm()    
    return render(request, "confirm.html", {'form': form})

def sushi_order(request):
    if request.method == "POST":
        form = SushiOrder(request.POST)

        if form.is_valid():
            form.save(commit=False)
            form.save()
        else:
            print('form invalid')
    form = SushiOrder()
    return render(request, "sushi/sushi.html", {'form':form})

class ConfirmList(generic.ListView):
    model = Confirm
    template_name = "confirm_order.html" 