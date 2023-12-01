from django import forms
from app.models import Eventlist

class AddEventsForm(forms.ModelForm):
    class Meta:
        model = Eventlist
        fields = ['title', 'date', 'time', 'location']

class SearchForm(forms.Form):
    title = forms.CharField(label='Search Event Title', max_length=100)
