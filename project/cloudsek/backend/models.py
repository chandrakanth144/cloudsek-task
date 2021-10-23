from enum import unique
from django.db import models

# Create your models here.

class calculate(models.Model):
    number1 = models.IntegerField(null=True)
    number2 = models.IntegerField(null=True)
    answer = models.IntegerField(null=True)
    #unique_identifier = models.AutoField(primary_key=True, unique=True)