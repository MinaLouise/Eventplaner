from typing import Any
from django import forms
from django.utils import timezone
from datetime import datetime

class AddEventsForm(forms.Form):
    title = forms.CharField(required=False)
    date = forms.DateField()
    time = forms.TimeField(required=False)
    location = forms.CharField(required=False)

class SearchEventForm(forms.Form):
    searchtitle = forms.CharField(required=False)