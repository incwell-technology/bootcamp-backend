from django.db import models
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, default="Bootcamp")       
    venue = models.CharField(max_length = 300, null=False, blank=False, default="Arun Thapa Chowk")
    description = models.TextField(null=False, blank=False, default="Lorem ipsum doler sit amet.")
    image = models.ImageField(upload_to="bootcamp/static/bootcamp/site-data/events", blank=False)
    date = models.DateField(null=False, blank=False, default=timezone.now)

    def __str__(self):
        return f'{self.title}'