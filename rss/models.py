from django.db import models
from django.contrib import admin

# Create your models here.
class Jobs(models.Model):
    title = models.CharField(max_length=30)
    jobdetails = models.TextField()
    key_skills = models.CharField(max_length=30)
    exp = models.IntegerField(default=0,blank=True)
    city = models.CharField(max_length=30,blank=True)
    state = models.CharField(max_length=30,blank=True)
    country = models.CharField(max_length=30,blank=True)    
    date_created = models.DateField(auto_now=True)
    salary = models.IntegerField(default=0)
    qualification = models.CharField(max_length=30,blank=True)
admin.site.register(Jobs)