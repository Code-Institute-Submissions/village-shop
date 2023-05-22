from django.db import models


class Event(models.Model):
    event_lead = models.CharField(max_length=50, null=False, blank=False)
    contact_email = models.EmailField(max_length=254, null=False, blank=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    event_date = models.CharField(max_length=15, null=False, blank=False)
    time = models.CharField(max_length=15, null=False, blank=False)


class Post(models.Model):
    title = models.CharField(max_length=100)
    intro = models.TextField()
    article = models.TextField()
    image = models.ImageField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

