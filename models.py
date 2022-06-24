from django.db import models
from django.conf import settings

class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(max_length=8)
    age = models.IntegerField(max_length=3)
    nationality = models.CharField(max_length=128)

class UserWOAcc(models.Model):
    email = models.EmailField(('email address'), blank=False, null=False, unique=True)


