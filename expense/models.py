from django.db import models
# from django.core.validators
# Create your models here.
class et(models.Model):
    months=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    amount=models.IntegerField()
    date=models.DateField()
