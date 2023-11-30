from django.http.request import HttpRequest
from django.shortcuts import render
from django.http.response import HttpResponse
from datetime import datetime
from app.forms import AddEventsForm
from app.models import Eventlist

# Create your views here.
def event_page(request:HttpRequest)->HttpResponse:
    if request.method == 'POST':
        form = AddEventsForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['Title']
            date = form.cleaned_data['Date']
            time = form.cleaned_data['Time']
            location = form.cleaned_data['location']

            propertime= datetime.strptime(time, '%I:%M %p').time()

            event = Eventlist(title=title, date=date, time=propertime, location="location")

            event.save()
            
            return HttpResponse('Form submitted successfully!')
        else:
            return render(request, "event.html", {"form":form})
    else:
        return render(request, "event.html", {"form":form})