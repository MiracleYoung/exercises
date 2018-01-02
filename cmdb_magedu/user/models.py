from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=128)
    age = models.IntegerField()
    telephone = models.CharField(max_length=32)
    email = models.EmailField()
    register_time = models.DateTimeField(auto_now_add=True)
    login_time = models.DateTimeField()