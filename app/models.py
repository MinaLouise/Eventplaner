from django.utils import timezone
from datetime import datetime
from django.db import models

# Create your models here.
class Eventlist(models.Model):
    title = models.TextField()
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=datetime.now)
    location = models.TextField()

    def propertime(self):
        return self.time.strftime('%I:%M %p')

def createEvent(title, date, time, location):
    event = Eventlist(title = title, date = date, time = time, location = location)
    event.save()
    return event
    
def read_all():
    return Eventlist.objects.all()

def search_by_title(title):
    try:
        return Eventlist.objects.get(title=title)
    except Eventlist.DoesNotExist:
        return None

def update(title, new_title, new_date, new_time, new_location):
    event = Eventlist.objects.get(title=title)
    event.title = new_title
    event.date = new_date
    event.time = new_time
    event.location = new_location
    event.save()
    return event

def delete(id):
    event = Eventlist.objects.get(id=id)
    event.delete()
    return event