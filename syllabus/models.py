from django.db import models
from django.utils.timezone import datetime


class Link(models.Model):
    link = models.CharField(max_length=500, null=False, blank=False, default="https://incwellventure.com")
    link_for = models.CharField(max_length=500, null=False, blank=False, default="Github")

    def __str__(self):
        return f'{self.link}: {self.link_for}'


class Course(models.Model):
    name = models.CharField(max_length=500, null=False, blank=True, default="Python")
    image = models.FileField(upload_to='syllabus/static/syllabus/site-data/course-pictures', blank=True)
    description = models.TextField(null=False, blank=False, default="Lorem ipsum")
    start_time = models.DateTimeField(default=datetime.now)
    end_time = models.DateTimeField(default=datetime.now)
    link = models.ManyToManyField(Link, related_name='course_links')

    def __str__(self):
        return f'{self.name}'