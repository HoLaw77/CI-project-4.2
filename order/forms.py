from django import forms
import datetime as dt


class BookTimeForm(forms.Form):
    Time = forms.CharField(max_length=100)
    Date = forms.CharField(widget=forms.Textarea)
    People = forms.CharField(widget=forms.Textarea)
