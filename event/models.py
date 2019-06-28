from django.db import models
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, default="Bootcamp")       
    venue = models.CharField(max_length = 300, null=False, blank=False, default="Arun Thapa Chowk")
    description = models.TextField(null=False, blank=False, default="Lorem ipsum doler sit amet.")
    image = models.ImageField(upload_to="bootcamp/static/bootcamp/site-data/events", blank=False)
    date = models.DateField(null=False, blank=False, default=timezone.now)
    from_time = models.TimeField(null=False, blank=False)
    to_time = models.TimeField(null=False, blank=False)

    def __str__(self):
        return f'{self.title}'


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class Main_Event(SingletonModel):
    title = models.CharField(max_length=200, null=False, blank=False, default="Bootcamp")       
    venue = models.CharField(max_length = 300, null=False, blank=False, default="Arun Thapa Chowk")
    description = models.TextField(null=False, blank=False, default="Lorem ipsum doler sit amet.")
    image = models.ImageField(upload_to="bootcamp/static/bootcamp/site-data/main-events", blank=False)
    date = models.DateField(null=False, blank=False, default=timezone.now)
    from_time = models.TimeField(null=False, blank=False)
    to_time = models.TimeField(null=False, blank=False)

    def __str__(self):
        return f'{self.title}'