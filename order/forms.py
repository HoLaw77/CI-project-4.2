from django import forms
from django.forms import ModelForm
from .models import Sushi, Confirm, Ramen, Drink


class BookTimeForm(forms.ModelForm):
     class Meta:
        model = Confirm
        fields = "__all__"

class SushiOrder(forms.ModelForm):
    class Meta:
        model = Sushi
        fields = ["NIGIRI_SUSHI", "INARI_SUSHI", "MAKI_SUSHI", "TEMAKI_SUSHI", "SOY_OIL", "WASABI"]

class RamenOrder(forms.ModelForm):
    class Meta:
        model = Ramen
        fields = ["toppings_choice", "side_dish", "soup_choice"]

class DrinkOrder(forms.ModelForm):
    class Meta:
        model = Drink
        fields = ["SAKE", "BEER", "CHOYA", "GREEN_TEA", "WATER" ]