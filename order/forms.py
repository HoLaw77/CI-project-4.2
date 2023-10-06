from django import forms
from django.forms import ModelForm
from .models import Sushi, Confirm, Ramen, Drink, Order


class BookTimeForm(forms.ModelForm):
     class Meta:
        model = Confirm
        fields = "__all__"

class SushiOrder(forms.ModelForm):
    class Meta:
        model = Sushi
        fields = ["NIGIRI_SUSHI", "INARI_SUSHI", "MAKI_SUSHI", "TEMAKI_SUSHI", "SOY_OIL", "WASABI"]
    # class Meta:
    #     model = Order
    #     fields = ['sushi']
class RamenOrder(forms.ModelForm):
    class Meta:
        model = Ramen
        fields = ["toppings_choice", "side_dish", "soup_choice"]

    # class Meta:
    #     model = Order
    #     fields = ['ramen']
class DrinkOrder(forms.ModelForm):
    class Meta:
        model = Drink
        fields = ["SAKE", "BEER", "CHOYA", "GREEN_TEA", "WATER" ]
    
    # class Meta:
    #     model = Order
    #     fields = ['drink']

class AddSushiOrder(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["sushi"]

class AddRamenOrder(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["ramen"]

class AddDrinkOrder(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["drink"]