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
    type = models.CharField(max_length=20, null=False, blank=False)
    phone = models.CharField(max_length=15,null=False, blank=False)

    def __str__(self):
        return f'{self.phone}'

class Company(SingletonModel):
    name = models.CharField(max_length=99)
    phone = models.ManyToManyField(PhoneNumber, related_name="company_phone")
    location = models.CharField(max_length=300, null=False, blank=False)
    

    def __str__(self):
        return f'{self.name}'


class Skill(models.Model):
    skill = models.CharField(max_length = 300, null=False, blank=False)

    def __str__(self):
        return f'{self.skill}'


class Mentor(models.Model):
    firstName = models.CharField(max_length = 300, null=False, blank=False)
    lastName = models.CharField(max_length = 300, null=False, blank=False)
    photo = models.FileField(upload_to='bootcamp/static/bootcamp/site-data/profile-pictures', blank=False)
    designation = models.CharField(max_length=300, null=False, blank=False)
    summary = models.TextField(null=False, blank=False)
    facebookUsername = models.CharField(max_length=800, null=False, blank=False)
    mediumUsername = models.CharField(max_length=800, null=False, blank=False)
    twitterUsername = models.CharField(max_length=800, null=False, blank=False)
    githubUsername = models.CharField(max_length=800, null=False, blank=False)
    linkedinUsername = models.CharField(max_length=800, null=False, blank=False)
    skill = models.ManyToManyField(Skill, related_name="mentor_skills")
    course = models.ManyToManyField(syllabus_models.Course, related_name="mentor_course")
    
    def __str__(self):
        return f'{self.firstName} {self.lastName}'


class Content(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False)
    image = models.FileField(upload_to='bootcamp/static/bootcamp/site-data/content-pictures', blank=True)
    description = models.TextField(null=False, blank=False)

    def __str__(self):
        return f'{self.title}'