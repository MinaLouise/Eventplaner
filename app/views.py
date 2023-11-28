from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from app.models import Eventlist

# Create your views here.
event = Eventlist

def events_list(request):
    return render(request, "index.html", {'event': event})

def event_detail(request: HttpRequest, team_name):
    title = event.get(team_name)  
    context = {'event': event}
    return render(request, 'event.html', {"form":form, "event":event})

