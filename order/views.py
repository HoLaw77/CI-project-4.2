from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Ramen, Sushi, Drink, Order, Confirm
from django.views import generic
from django.views.generic import TemplateView, DetailView
from django.contrib import admin


from .forms import BookTimeForm, SushiOrder, RamenOrder, DrinkOrder


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


def order(request):
    order = Order.objects.filter(customer=request.user, confirmed=False).last()
    if order is not None:
        return render(request, "order.html", {'order': order})
    else:
        return render(request, "order.html")


def confirm_order(request):
    if request.method == "POST":
        form = BookTimeForm(request.POST)
        if form.is_valid():
            order_id = request.POST.get('id')
            order = Order.objects.get(id=order_id)
            order.confirmed = True
            order.save()
            confirm = form.save(commit=False)
            confirm.order = order
            confirm.save()
        else:
            print("form invalid")
    order = Order.objects.filter(customer=request.user, confirmed=False).last()
    if order is not None:
        if confirm is not None:
            print(confirm.your_name)
            return render(
                request,
                "confirm_order.html",
                {"confirm": confirm}
            )

    return render(
        request,
        "confirm_order.html",
        {"confirm": confirm}
    )


def sushi_order(request):
    if request.method == "POST":
        form = SushiOrder(request.POST)
        if form.is_valid():
            form.save(commit=False)
            order = Order.objects.filter(
                customer=request.user, confirmed=False).last()
            if order is not None and not order.confirmed:
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
            form = SushiOrder()
            return render(request, "sushi/sushi.html", {'form': form})
    form = SushiOrder()
    return render(request, "sushi/sushi.html", {'form': form})


def ramen_order(request):
    if request.method == "POST":
        form = RamenOrder(request.POST)
        if form.is_valid():
            form.save(commit=False)
            order = Order.objects.filter(
                customer=request.user, confirmed=False).last()
            if order is not None and not order.confirmed:
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
            form = RamenOrder()
            return render(request, "ramen/ramen.html", {'form': form})
    form = RamenOrder()
    return render(request, "ramen/ramen.html", {'form': form})


def drink_order(request):
    if request.method == "POST":
        form = DrinkOrder(request.POST)
        if form.is_valid():
            form.save(commit=False)
            order = Order.objects.filter(
                customer=request.user, confirmed=False).last()
            if order is not None and not order.confirmed:
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
            form = DrinkOrder()
            return render(request, "drink/drink.html", {'form': form})
    form = DrinkOrder()
    return render(request, "drink/drink.html", {'form': form})


def delete_ramen_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.ramen = None
    order.save()
    return redirect(ramen_order)


def delete_sushi_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.sushi = None
    order.save()
    return redirect(sushi_order)


def delete_drink_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order.drink = None
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
