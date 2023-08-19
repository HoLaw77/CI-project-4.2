from django import forms


class BookTimeForm(forms.Form):
    book_time = forms.CharField(label="Book Time", max_length=100)