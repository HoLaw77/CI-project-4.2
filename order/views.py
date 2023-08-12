from django.http import HttpResponse
from django.shortcuts import render
from .models import Ramen, Sushi, Drink, Order
from django.views import generic
# Create your views here.


def HttpResponde(request):
    return render(request, 'templates/index.html')


class SushiList (generic.Listview):
    model = Sushi
    queryset = Sushi.object.filter(status=1).order_by('-created_on')
    template_name="index.html"
    paginated_by = 3
