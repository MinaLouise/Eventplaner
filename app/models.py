from django.db import models

class EventlistManager(models.Manager):
    def create_list(self, items, complete):
        event_list = self.create(items=items, complete=complete)
        return event_list

    def view_list(self):
        return self.all()

    def search_list(self, items):
        try:
            return self.get(items=items)
        except self.model.DoesNotExist:
            return None

    def filter_complete(self, complete):
        return self.filter(complete=complete)

    def update_list(self, items, completed):
        event_list = self.get(items=items)
        event_list.complete = completed
        event_list.save()
        return event_list

    def delete_item(self, items):
        event_list = self.get(items=items)
        event_list.delete()
        return event_list

class Eventlist(models.Model):
    items = models.TextField()
    complete = models.BooleanField(default=False)

    objects = EventlistManager()

    def __str__(self):
        return self.items
