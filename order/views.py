from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Ramen, Sushi, Drink, Order, Confirm
from django.views import generic
from django.views.generic import TemplateView, DetailView
from django.contrib import admin


from .forms import BookTimeForm, SushiOrder, RamenOrder, DrinkOrder
# Create your views here.

def sushi(request):
    return render(request, 'sushi/sushi.html')


def ramen(request):
    return render(request, 'ramen/ramen.html')

def drink(request):
    return render(request, 'drink/drink.html')

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

def ramen_order(request):
    if request.method == "POST":
        form = RamenOrder(request.POST)

        if form.is_valid():
            form.save(commit=False)
            form.save()
        else:
            print('form invalid')
    form = RamenOrder()
    return render(request, "ramen/ramen.html", {'form':form})

def drink_order(request):
    if request.method == "POST":
        form = DrinkOrder(request.POST)

        if form.is_valid():
            form.save(commit=False)
            form.save()
        else:
            print('form invalid')
    form = DrinkOrder()
    return render(request, "drink/drink.html", {'form':form})

def delete_drink_order(request, drink_order_id):
    order = get_object_or_404(order.drink, id=drink_order_id)
    order.delete()
    return redirect(drink_order)
