from django.http.request import HttpRequest
from django.shortcuts import render
from django.http.response import HttpResponse
from app import models
from app.forms import AddEventsForm

# Create your views here.
def event_page(request:HttpRequest)->HttpResponse:
    form = AddEventsForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data['Title']
        date = form.cleaned_data['Date']
        time = form.cleaned_data['Time']
        location = form.cleaned_data['Location']
        return render(request, "event.html", {"form": form, "Title":title, "Date":date, "Time":time, "Location":location})
    else:
        return render(request, "event.html", {"form":form})