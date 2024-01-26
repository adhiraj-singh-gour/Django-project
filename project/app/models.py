from django.db import models

# Create your models here.

# user Registration
class Userregister(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Password = models.CharField(max_length=100)
    Cpassword = models.CharField(max_length=100)
    Profile = models.FileField()
    
