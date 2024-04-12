from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    desciption = models.TextField()
    count = models.IntegerField()
    is_active = models.BooleanField()

class Category(models.Model):
    name = models.CharField(max_length=255)