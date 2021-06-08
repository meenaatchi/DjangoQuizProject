from django.db import models


# Create your models here.



class Newuser(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
