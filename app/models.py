from django.db import models

# Create your models here.

def create_list(event, complete):
    event_list = Todolist(event=event, complete=complete)
    event_list.save()
    return event_list

def view_list():
    return Todolist.objects.all()

def search_list(event):
    try:
        return Todolist.objects.get(event=event)
    except Todolist.DoesNotExist:
        return None

def filter_complete(complete):
    return Todolist.objects.filter(complete=complete)

def update_list(event, completed):
    event_list = Todolist.objects.get(event=event)
    event_list.complete = completed
    event_list.save()
    return event_list

def delete_item(event):
    event_list = Todolist.objects.get(event=event)
    event_list.delete()
    return event_list