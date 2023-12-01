from django.http.request import HttpRequest
from django.shortcuts import render
from django.http.response import HttpResponse
from datetime import datetime
from app.forms import AddEventsForm
from app.models import Eventlist

# Create your views here.
events = []

def event_page(request:HttpRequest)->HttpResponse:
    form = AddEventsForm(request.POST)
    if form.is_valid():

        form.save()
        events = Eventlist.objects.all()
        
        return render(request, "index.html", {"form":form, "events": events})
    else:
        events = Eventlist.objects.all()
        return render(request, "index.html", {"form":form, "events": events})
        

def searching_page(request:HttpRequest)->HttpResponse:
    form = AddEventsForm(request.POST)
    if form.is_valid():
        
        events = Eventlist.objects.all()
            
        return render(request, "event.html", {"form":form, "events": events})
    else:
        events = Eventlist.objects.all()
        return render(request, "event.html", {"form":form, "events": events})