from django.db import models
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class Event(models.Model):
    event_id = models.CharField(max_length=32, null=False, editable=False)
    event_lead = models.CharField(max_length=50, null=False, blank=False)
    contact_email = models.EmailField(max_length=254, null=False, blank=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=400, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=False, null=False, blank=False)
    time = models.CharField(max_length=15, null=False, blank=False)

class Attendee(models.Model):
    attendee_number = models.CharField(max_length=32, null=False, editable=False)
    attendee_name = models.CharField(max_length=50, null=False, blank=False)
    attendee_email = models.EmailField(max_length=254, null=False, blank=False)
    event = models.ForeignKey('Event', null=True, blank=True, on_delete=models.SET_NULL)
