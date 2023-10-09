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
        fields = ["nigiri_sushi", "inari_sushi", "maki_sushi", "temaki_sushi", "soy_oil", "wasabi"]
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
        fields = ["sake", "beer", "choya", "green_tea", "water" ]
    
    # class Meta:
    #     model = Order
    #     fields = ['drink']
    #​
# class AddSushiOrder(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ["sushi"]

# class AddRamenOrder(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ["ramen"]

# class AddDrinkOrder(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ["drink"]