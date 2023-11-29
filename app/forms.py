from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class Eventsearch(forms.Form):
    searchbar = forms.CharField()

class EventAdd(forms.Form):
    adding = forms.CharField()