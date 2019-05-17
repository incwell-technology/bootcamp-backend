from django.db import models
from django.utils.timezone import datetime
from syllabus import models as syllabus_models
from django.contrib.auth.models import User
from django.contrib import admin

gender_choice = (
    (True, 'Male'),
    (False, 'Female'),
)

class StudentEnroll(models.Model):
    fullName = models.CharField(max_length=400, null=False, blank=False)
    email = models.CharField(max_length=600, null=False, blank=False)
    gender = models.BooleanField(max_length=1, choices=gender_choice, null=False, blank=False)
    education = models.CharField(max_length=800, null=False, blank=False)
    phone = models.CharField(max_length=500, null=False, blank=False)
    gitLink = models.CharField(max_length=800, null=True, blank=True)
    course = models.ManyToManyField(syllabus_models.Course, related_name="student_course")
    firstName = models.CharField(max_length=300, null=False, blank=False)
    middleName = models.CharField(max_length = 300, null=True, blank=True)
    lastName = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return f'{self.fullName}'


class Talk_To_Mentor(models.Model):
    fullName = models.CharField(max_length = 300, null=False, blank=False)
    email = models.EmailField(max_length=70,blank=False, null=False)
    skypeId = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return f'{self.fullName}'


class Scholarship(models.Model):
    reason = models.CharField(max_length=800, null=False, blank=False)
    projectLink = models.CharField(max_length=300, null=False, blank=False)
    planToContribute = models.TextField(null=False, blank=False)
    education = models.CharField(max_length=500, null=False, blank=False)
    university = models.CharField(max_length=300, null=False, blank=False)
    email = models.CharField(max_length=200, null=False, blank=False)
    fullName = models.CharField(max_length=500, null=False, blank=False)
    phone = models.CharField(max_length=400, null=False, blank=False)

    def __str__(self):
        return f'{self.fullName}'
        