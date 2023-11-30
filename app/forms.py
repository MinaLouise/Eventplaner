from django import forms


class AddEventsForm(forms.Form):
    title = forms.CharField()
    date = forms.DateField()
    time = forms.CharField()
    location = forms.CharField()