from django.db import models
from django.utils.timezone import datetime
from syllabus import models as syllabus_models

gender_choice = (
    (True, 'Male'),
    (False, 'Female'),
)

class Student(models.Model):
    firstName = models.CharField(max_length = 300, null=False, blank=False)
    middleName = models.CharField(max_length = 300, null=True, blank=True)
    lastName = models.CharField(max_length = 300, null=False, blank=False)
    email = models.EmailField(max_length=70,blank=False, null= False, unique= True) 
    gender = models.BooleanField(max_length=1, choices=gender_choice, null=False, blank=False)
    education = models.CharField(max_length=800, null=False, blank=False)
    phone = models.CharField(max_length=500, null=False, blank=False)
    gitLink = models.CharField(max_length=800, null=True, blank=True)
    course = models.ManyToManyField(syllabus_models.Course, related_name="student_course")

    def __str__(self):
        return f'{self.firstName} {self.middleName} {self.lastName}'

    def save(self, *args, **kwargs):
        student = super(Student, self).save(*args, **kwargs)   
        

class Enroll(models.Model):
    student = models.ManyToManyField(Student, related_name="enroll_student")
    course = models.ManyToManyField(syllabus_models.Course, related_name="enroll_course")
    
    def __str__(self):
        return f'{self.student}'
        

class Talk_To_Mentor(models.Model):
    firstName = models.CharField(max_length = 300, null=False, blank=False)
    lastName = models.CharField(max_length = 300, null=False, blank=False)
    email = models.EmailField(max_length=70,blank=False, null=False)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'






