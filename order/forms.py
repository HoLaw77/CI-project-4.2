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
        fields = "__all__"

class RamenOrder(forms.ModelForm):
    class Meta:
        model = Ramen
        fields = "__all__"

class DrinkOrder(forms.ModelForm):
    class Meta:
        model = Drink
        fields = "__all__"