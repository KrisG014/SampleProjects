from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import datetime

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    first_name = models.CharField(max_length=25) 
    last_name = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=25)
    is_admin = models.BooleanField(default=False)
 
    
    def __str__(self):
        return self.username
    
    def FirstName(self):
        return first_name
    
    def LastName(self):
        return last_name    

    def FullName(self):
        return first_name + " " + last_name    

    def Email(self):
        return email   
    
    def Password(self):
        return password      

    def IsAdmin(self):
        return is_admin      
    
    def get_absolute_url(self):
        return reverse('URLShortener:userurls', kwargs={'pk': self.username})

class URLEntry(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    original_url = models.URLField(max_length=300)
    shortened_url = models.URLField()    
    created_date = models.DateTimeField('date created')
    
    def __str__(self):
        return self.original_url
    
    def Username(self):
        return username    
    
    def ShortenedURL(self):
        return shortened_url   

    def CreatedDate(self):
        return created_date

    def get_absolute_url(self):
        return reverse('URLShortener:userurls', kwargs={'pk': self.username})