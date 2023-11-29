from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.views import View
from django.http import JsonResponse
from app.models import Eventlist
from app.forms import LoginForm, EventAdd, Eventsearch

# Create your views here.
def login_page(request:HttpRequest)->HttpResponse:
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page or to the events page
                return redirect('event.html')  # Adjust 'events' to your events URL name
    else:
        form = LoginForm()
    
    return render(request, 'loginpage.html', {'form': form})


def event_page(request:HttpRequest)->HttpResponse:
    form1 = Eventsearch
    form2 = EventAdd
    if form1.is_valid():
        searchbar = form1.cleaned_data['searchbar']
        return render(request, "event.html", {'form1': form1})
    elif form2.is_valid():
        adding = form2.cleaned_data['adding']
        return render(request, "event.html", {'form2':form2})
    else:
        return None



class EventOperations(View):
    def get(self, request):
        events = Eventlist.objects.view_list()
        serialized_events = self.serialize_events(events)
        return JsonResponse(serialized_events, safe=False)

    def post(self, request):
        items = request.POST.get('items')
        complete = request.POST.get('complete', False)
        new_event = Eventlist.objects.create_list(items, complete)
        return JsonResponse({'message': 'Event created successfully'})

    def put(self, request):
        items = request.POST.get('items')
        complete = request.POST.get('complete')
        Eventlist.objects.update_list(items, complete)
        return JsonResponse({'message': 'Event updated successfully'})

    def delete(self, request):
        items = request.POST.get('items')
        Eventlist.objects.delete_item(items)
        return JsonResponse({'message': 'Event deleted successfully'})

    def serialize_events(self, events):
        serialized = [{'items': event.items, 'complete': event.complete} for event in events]
        return serialized

