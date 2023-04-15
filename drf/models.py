from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class menu(models.Model):
    item = models.CharField(max_length=150)
    price = models.IntegerField()