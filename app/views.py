from django.http.request import HttpRequest
from django.shortcuts import render
from django.http.response import HttpResponse
from app import models
from app.forms import AddEventsForm

# Create your views here.
def event_page(request:HttpRequest)->HttpResponse:
    form = AddEventsForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data['title']
        date = form.cleaned_data['date']
        time = form.cleaned_data['time']
        location = form.cleaned_data['location']
        return render(request, "event.html", {"form": form, "Title":title, "Date":date, "Time":time, "Location":location})
    else:
        return render(request, "event.html", {"form":form})