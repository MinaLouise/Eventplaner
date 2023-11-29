from django.db import models

# Create your models here.
class Eventlist(models.Model):
    title = models.CharField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField()

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