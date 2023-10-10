from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, reverse
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

def login_user(request):
    return render(request, 'account/login_user.html')
    
def logout_user(request):
    return render(request, 'account/logout_user.html')

class SushiList(generic.ListView):
    model = Sushi
    template_name = "index.html"
    paginated_by = 3
# class OrderList(generic.ListView):
#     model = Order
#     template_name = "order.html"
#     paginated_by = 1

def order(request):
    order = Order.objects.filter(customer=request.user, confirmed=False).last()
    if order is not None:
        print('order is not none')
        return render(request, "order.html", {'order': order})
    else:
        print('order is none')
        return render(request, "order.html")

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
        # form = AddSushiOrder(request.POST)
        #​
        if form.is_valid():
            form.save(commit=False)
            order = Order.objects.filter(customer=request.user, confirmed=False).last()
            if order is not None:
                order.sushi = form.save()
                order.save()
            else:
                order = Order.objects.create(customer=request.user)
                order.sushi = form.save()
                order.save()
            if order.ramen is None:
                return redirect(ramen_order)
            elif order.drink is None:
                return redirect(drink_order)
            else:
                return redirect(reverse('order'))
            
            
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
        # form = AddRamenOrder(request.POST)

        if form.is_valid():
            form.save(commit=False)
            order = Order.objects.filter(customer=request.user, confirmed=False).last()
            if order is not None:
                order.ramen = form.save()
                order.save()
            else:
                order = Order.objects.create(customer=request.user)
                order.ramen = form.save()
                order.save()
            if order.sushi is None:
                return redirect(sushi_order)
            elif order.drink is None:
                return redirect(drink_order)
            else:
                return redirect(reverse('order'))
            
        else:
            print('form invalid')
    form = RamenOrder()
    return render(request, "ramen/ramen.html", {'form':form})

def drink_order(request):
    if request.method == "POST":
        form = DrinkOrder(request.POST)
        # form = AddDrinkOrder(request.POST)

        if form.is_valid():
            form.save(commit=False)
            order = Order.objects.filter(customer=request.user, confirmed=False).last()
            if order is not None:
                order.drink = form.save()
                order.save()
            else:
                order = Order.objects.create(customer=request.user)
                order.drink = form.save()
                order.save()
            if order.sushi is None:
                return redirect(sushi_order)
            elif order.ramen is None:
                return redirect(ramen_order)
            else:
                return redirect(reverse('order'))
            
            
        else:
            print('form invalid')
    form = DrinkOrder()
    return render(request, "drink/drink.html", {'form':form})

def delete_ramen_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.ramen= None
    order.save()
    return redirect(ramen_order)

def delete_sushi_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.sushi= None
    order.save()
    return redirect(sushi_order)

def delete_drink_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.drink= None
    order.save()
    return redirect(drink_order)

def edit_ramen_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    form = RamenOrder(instance=order)
    order.save()
    return redirect(ramen_order)

def edit_sushi_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    form = SushiOrder(instance=order)
    order.save()
    return redirect(sushi_order)

def edit_drink_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    form = DrinkOrder(instance=order)
    order.save()
    return redirect(drink_order)