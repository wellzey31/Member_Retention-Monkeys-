from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user_id = models.IntegerField()
    email = models.CharField(max_length=255)
    phone = models.IntegerField()
    age = models.IntegerField()
    occupation = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    joined_date = models.DateField()
    
    