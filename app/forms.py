from django import forms
from django.utils import timezone
from datetime import datetime

class AddEventsForm(forms.Form):
    title = forms.CharField()
    date = forms.DateField()
    time = forms.TimeField()
    location = forms.CharField()

class SearchEventForm(forms.Form):
    searchtitle = forms.CharField(required=False)