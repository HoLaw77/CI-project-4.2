from django import forms
import datetime as dt


class BookTimeForm(forms.Form):
    Name = forms.CharField(max_length=100)
    Time = forms.CharField(max_length=100)
    Date = forms.CharField(widget=forms.Textarea)
    People = forms.CharField(widget=forms.Textarea)
    Email = forms.CharField(max_length=100)
