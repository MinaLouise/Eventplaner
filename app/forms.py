from django import forms
from app.models import Eventlist

class AddEventsForm(forms.ModelForm):
    class Meta:
        model = Eventlist
        fields = ['title', 'date', 'time', 'location']