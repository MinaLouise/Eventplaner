from typing import Any
from django import forms
from django.utils import timezone
from datetime import datetime

class AddEventsForm(forms.Form):
    title = forms.CharField(required=True, error_messages={"required":""}, widget=forms.TextInput(attrs={'placeholder': 'Your event', 'required': 'true'}))
    date = forms.DateField(required=True, error_messages={"required":""}, widget=forms.TextInput(attrs={'placeholder': 'Event date', 'required': 'true'}))
    time = forms.TimeField(required=True, error_messages={"required":""}, widget=forms.TextInput(attrs={'placeholder': 'Event time', 'required': 'true'}))
    location = forms.CharField(required=True, error_messages={"required":""}, widget=forms.TextInput(attrs={'placeholder': 'Event location', 'required': 'true'}))

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

class SearchEventForm(forms.Form):
    searchtitle = forms.CharField(required=False)