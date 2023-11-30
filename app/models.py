from django.utils import timezone
from datetime import datetime
from django.db import models

# Create your models here.
class Eventlist(models.Model):
    title = models.CharField(max_length=100, default="name of event")
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=datetime.now)
    location = models.CharField(max_length=100, default='event location')

    def propertime(self):
        return self.time.strftime('%I:%M %p')

def createEvent(title, date, time, location):
    event = Eventlist(title = title, date = date, time = time, location = "location")
    event.save()
    return event
    
def read_all():
    return Eventlist.objects.all()

def search_by_title(title):
    try:
        return Eventlist.objects.get(title=title)
    except Eventlist.DoesNotExist:
        return None
    
def filter_by_date(date):
    return Eventlist.objects.filter(date=date)

def update(title, new_date):
    event = Eventlist.objects.get(title=title)
    event.date = new_date
    event.save()
    return event

def delete(title):
    event = Eventlist.objects.get(title=title)
    event.delete()
    return event