from django.db import models
from django.utils.timezone import datetime
from syllabus import models as syllabus_models


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


class PhoneNumber(models.Model):
    type = models.CharField(max_length=300, null=False, blank=False, default="Mobile")
    phone = models.IntegerField(null=False, blank=False, default="98000000")

    def __str__(self):
        return f'{self.phone}'

class Company(SingletonModel):
    name = models.CharField(max_length=99, default="Incwell Technology")
    phone = models.ManyToManyField(PhoneNumber, related_name="company_phone")
    location = models.CharField(max_length=300, null=False, blank=False, default="Arun thapa Chowk")
    

    def __str__(self):
        return f'{self.name}'


class Skill(models.Model):
    skill = models.CharField(max_length = 300, null=False, blank=False, default="DevOps")

    def __str__(self):
        return f'{self.skill}'


class Mentor(models.Model):
    firstName = models.CharField(max_length = 300, null=False, blank=False, default="John")
    lastName = models.CharField(max_length = 300, null=False, blank=False, default="Doe")
    photo = models.FileField(upload_to='bootcamp/static/bootcamp/site-data/profile-pictures', blank=True)
    designation = models.CharField(max_length=300, null=False, blank=False, default="Software Engineer")
    summary = models.TextField(null=False, blank=False, default="Lorem ipsum")
    facebookUsername = models.CharField(max_length=800, null=False, blank=False, default="username")
    mediumUsername = models.CharField(max_length=800, null=False, blank=False, default="username")
    twitterUsername = models.CharField(max_length=800, null=False, blank=False, default="username")
    githubUsername = models.CharField(max_length=800, null=False, blank=False, default="username")
    linkedinUsername = models.CharField(max_length=800, null=False, blank=False, default="username")
    skill = models.ManyToManyField(Skill, related_name="mentor_skills")
    course = models.ManyToManyField(syllabus_models.Course, related_name="mentor_course")
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Content(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False, default="About Us")
    image = models.FileField(upload_to='bootcamp/static/bootcamp/site-data/content-pictures', blank=True)
    description = models.TextField(null=False, blank=False, default="Lorem ipsum")

    def __str__(self):
        return f'{self.title}'