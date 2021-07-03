from django.db import models
from django.db.models.base import Model

# Create your models here.
class Contact (models.Model):
    Email = models.CharField( max_length=120)
    Address = models.CharField(max_length=120)
    Firstname = models.CharField(max_length=120)
    Lastname = models.CharField(max_length=120)
    # date = models.DateField(),
   
class Image (models.Model):
    Image = models.ImageField(upload_to="img/%y")
    Description = models.CharField(max_length=120)
    def __str__(self):
        return self.Description