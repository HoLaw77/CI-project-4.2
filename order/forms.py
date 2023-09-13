from django import forms
from django.forms import ModelForm
from .models import Sushi, Confirm, Ramen


class BookTimeForm(forms.ModelForm):
     class Meta:
        model = Confirm
        fields = "__all__"

class SushiOrder(forms.ModelForm):
    class Meta:
        model = Sushi
        fields = ['NIGIRI_SUSHI']

class RamenOrder(forms.ModelForm):
    class Meta:
        model = Ramen
        fields = "__all__"