from django.db import models
from django.utils.timezone import datetime


class Link(models.Model):
    link = models.CharField(max_length=500, null=False, blank=False)
    linkFor = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return f'{self.link}: {self.linkFor}'


class Course(models.Model):
    name = models.CharField(max_length=500, null=False, blank=False)
    image = models.FileField(upload_to='bootcamp/static/bootcamp/site-data/course-pictures', blank=False)
    description = models.TextField(null=False, blank=False)
    startTime = models.DateTimeField(default=datetime.now)
    endTime = models.DateTimeField(default=datetime.now)
    link = models.ManyToManyField(Link, related_name='course_links')

    def __str__(self):
        return f'{self.name}'