from django import forms
from django.forms import ModelForm
from .models import Sushi, Confirm, Ramen, Drink, Order


class BookTimeForm(forms.ModelForm):
    class Meta:
        model = Confirm
        fields = ["your_name", "dinning_time",
                  "arriving_date", "number_of_people", "email"]


class SushiOrder(forms.ModelForm):
    class Meta:
        model = Sushi
        fields = ["nigiri_sushi", "inari_sushi",
                  "maki_sushi", "temaki_sushi", "soy_oil", "wasabi"]


class RamenOrder(forms.ModelForm):
    class Meta:
        model = Ramen
        fields = ["toppings_choice", "side_dish", "soup_choice"]


class DrinkOrder(forms.ModelForm):
    class Meta:
        model = Drink
        fields = ["sake", "beer", "choya", "green_tea", "water"]
