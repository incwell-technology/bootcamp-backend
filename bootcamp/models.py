from django.db import models
from django.utils.timezone import datetime


# Create your models here.
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


class Company(SingletonModel):
    name = models.CharField(max_length=99, default="Incwell Technology")
    phone = models.IntegerField(default="5200000,5200001")
    location = models.CharField(max_length=300, null=False, blank=False, default="Arun thapa Chowk")

    def __str__(self):
        return f'{self.name}'


class Skill(models.Model):
    skill = models.CharField(max_length = 300, null=False, blank=False, default="DevOps")

    def __str__(self):
        return f'{self.skill}'


class Mentor(models.Model):
    first_name = models.CharField(max_length = 300, null=False, blank=False, default="John")
    last_name = models.CharField(max_length = 300, null=False, blank=False, default="Doe")
    photo = models.FileField(upload_to='bootcamp/static/bootcamp/site-data/profile-pictures', blank=True)
    designation = models.CharField(max_length=300, null=False, blank=False, default="Software Engineer")
    summary = models.TextField(null=False, blank=False, default="Lorem ipsum")
    fb_link = models.CharField(max_length=800, null=False, blank=False, default="https://fb.com")
    medium_link = models.CharField(max_length=800, null=False, blank=False, default="https://medium.com")
    twitter_link = models.CharField(max_length=800, null=False, blank=False, default="https://twitter.com")
    github_link = models.CharField(max_length=800, null=False, blank=False, default="https://github.com")
    linkedIn_link = models.CharField(max_length=800, null=False, blank=False, default="https://linkedin.com")
    skill = models.ManyToManyField(Skill, related_name="mentor_skills")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Content(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False, default="About Us")
    image = models.FileField(upload_to='bootcamp/static/bootcamp/site-data/content-pictures', blank=True)
    description = models.TextField(null=False, blank=False, default="Lorem ipsum")

    def __str__(self):
        return f'{self.title}'