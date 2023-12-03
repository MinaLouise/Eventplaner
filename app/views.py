from django.http.request import HttpRequest
from django.shortcuts import redirect, render
from django.http.response import HttpResponse, HttpResponseNotFound
from datetime import datetime
from app.forms import AddEventsForm, SearchEventForm
from app.models import createEvent, read_all, delete, search_by_title

# Create your views here.
events = []

def form_page(request:HttpRequest)->HttpResponse:
    form = AddEventsForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data["title"]
        date = form.cleaned_data["date"]
        time = form.cleaned_data["time"]
        location = form.cleaned_data["location"]
        createEvent(title, date, time, location).save()
        events = read_all()
        return render(request, "form.html", {"form":form, "events": events})
    else:
        events = read_all()
        return render(request, "form.html", {"form":form, "events": events})
        

def events_page(request:HttpRequest)->HttpResponse:
    form = SearchEventForm(request.POST)
    if form.is_valid():
        searchtitle = form.cleaned_data["searchtitle"]
        search_title = search_by_title(searchtitle)
        events = read_all()
            
        return render(request, "event.html", {"form":form, "events": events, "search_title": search_title})
    else:
        events = read_all()
        return render(request, "event.html", {"form":form, "events": events})
    
def delete_event(request:HttpRequest, id)->HttpResponse:
    # if title in events:
        if request.method == 'POST':
            event = delete(id=id)
            event.delete()
            return redirect('events')
        return render(request, 'delete.html')
    # else:
    #     return HttpResponseNotFound('<h1>Event Not Found</h1>')