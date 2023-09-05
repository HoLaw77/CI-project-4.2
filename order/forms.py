from django import forms
from django.forms import ModelForm
from .models import Confirm


class BookTimeForm(forms.ModelForm):
    class Meta:
        model = Confirm
        fields = "__all__"
    
    def create(self, request):
        return {
            'Name': BookTimeForm.instance.your_name,
            'Time': BookTimeForm.instance.time,
            'Date': BookTimeForm.instance.date,
            'People': BookTimeForm.instance.number_of_people,
            'Email': BookTimeForm.instance.email
        }
    
    def save(request):
        BookTimeForm.save(request)
