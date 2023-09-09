from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Ramen, Sushi, Drink, Order, Confirm
from django.views import generic
from django.views.generic import TemplateView, DetailView
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


def confirm(request):
    return render(request, 'confirm.html')


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
        # name = request.POST.get('your_name')
        # time = request.POST.get('dinning_time')
        # date = request.POST.get('arriving_date')
        # people = request.POST.get('number_of_people')
        # email = request.POST.get('email')
        if form.is_valid():
            form.save(commit = False)
            form.save()
            # Confirm.objects.create(name=name, time=time, date=date, people=people, email=email)
        else:
            print('form invalid')

    form = BookTimeForm()    
    return render(request, "confirm.html", {'form': form})



