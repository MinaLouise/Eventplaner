from django.db import models

# Create your models here.
class Eventlist(models.Model):
    items = models.TextField()
    complete = models.BooleanField(default=False)

    def create_list(event, complete):
        event_list = Eventlist(event=event, complete=complete)
        event_list.save()
        return event_list

    def view_list():
        return Eventlist.objects.all()

    def search_list(event):
        try:
            return Eventlist.objects.get(event=event)
        except Eventlist.DoesNotExist:
            return None

    def filter_complete(complete):
        return Eventlist.objects.filter(complete=complete)

    def update_list(event, completed):
        event_list = Eventlist.objects.get(event=event)
        event_list.complete = completed
        event_list.save()
        return event_list

    def delete_item(event):
        event_list = Eventlist.objects.get(event=event)
        event_list.delete()
        return event_list