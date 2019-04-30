from django.db import models
from django.utils.timezone import datetime


class Enroll(models.Model):
    first_name = models.CharField(max_length = 300, null=False, blank=False, default="John")
    middle_name = models.CharField(max_length = 300, null=True, blank=True)
    last_name = models.CharField(max_length = 300, null=False, blank=False, default="Doe")
    email = models.EmailField(max_length=70,blank=False, null= False, unique= True)
    gender = models.BooleanField(default=True) #True=Male
    education = models.CharField(max_length=800, null=False, blank=False, default="Incwell Bootcamp")
    phone = models.CharField(max_length=500, null=False, blank=False, default="9800000")
    git_link = models.CharField(max_length=800, null=True, blank=True, default="No Git link")


    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'


class Talk_To_Mentor(models.Model):
    first_name = models.CharField(max_length = 300, null=False, blank=False, default="John")
    last_name = models.CharField(max_length = 300, null=False, blank=False, default="Doe")
    email = models.EmailField(max_length=70,blank=False, null=False,default="noemail@email.com")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'