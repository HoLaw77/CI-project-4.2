from django import forms
from django.forms import ModelForm
from .models import Confirm


class BookTimeForm(ModelForm):
    class Meta:
        model = Confirm
        fields = "__all__"
