from django.db import models


class Contact(models.Model):
    email = models.CharField( max_length=120)
    address = models.CharField(max_length=120)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
   

class Image(models.Model):
    image = models.ImageField(upload_to="img/%y")
    description = models.CharField(max_length=120)
    
    def __str__(self):
        return self.Description
