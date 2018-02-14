from __future__ import unicode_literals

from django.contrib.auth.hashers import make_password
from django.db import models
import uuid

from rest_framework import serializers
import six
from django.contrib.auth.models import User, AbstractUser


# Create your models here.
from mylib.image import scramble


class MyUser(AbstractUser):
    SEX=(('MALE','Male'),('FEMALE','Female'),('NS','Not Set'))
    # TYPE=(('AT','Attendee'),('OG','Organizer'))
    phone=models.CharField(max_length=50,null=True,blank=True)
    google_profile_image=models.URLField(max_length=200,blank=True,null=True)
    dob=models.DateField(null=True,blank=True)
    bio=models.CharField(max_length=100,null=True,blank=True)
    image=models.ImageField("uploads",upload_to=scramble,null=True,blank=True)
    gender=models.CharField(max_length=5,choices=SEX,default='NS')
    allow_notification=models.BooleanField(default=True,)

def save(self, *args, **kwargs):
    self.password = make_password(self.password)
    super(MyUser, self).save(*args, **kwargs)



    #bookings=models.

# class Client(AbstractUser):
#     id = models.CharField(primary_key=True ,max_length=20)
#     phone = models.CharField(max_length=20,null=True,blank=True)



