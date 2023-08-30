from django import forms
import datetime as dt


class BookTimeForm(forms.Form):
    Name = forms.CharField(max_length=100)
    Time = forms.TimeField()
    Date = forms.DateField()
    People = forms.IntegerField()
    Email = forms.EmailField(max_length=100)
