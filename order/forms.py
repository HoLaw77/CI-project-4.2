from django import forms
from django.forms import ModelForm
from .models import Confirm


class BookTimeForm(forms.ModelForm):
     class Meta:
        model = Confirm
        fields = ['name', 'time', 'date', 'people','email']
