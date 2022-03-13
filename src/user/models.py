from django.db import models
from django.utils import timezone

# Create your models here.
# Database initilization
class User(models.Model):
    name = models.CharField(max_length=120)
    username = models.CharField(max_length=40, unique=True)
    roll = models.CharField(max_length=10, unique=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    roles = models.CharField(max_length=10)  # patient doctor hcadmin accounts

    def __str__(self):
        return self.name