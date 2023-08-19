from django import forms
import datetime as dt

class ReservationForm(forms.Form):
    Time = forms.CharField(max_length=100)
    Date = forms.CharField(widget=forms.Textarea)
    Number of people = forms.CharField(widget=forms.Textarea)
    