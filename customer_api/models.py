from django.db import models
# from django.contrib.postgres.fields import EmailField

class Customer(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(max_length=40)
    child_first_name = models.CharField(max_length=32)
    child_last_name = models.CharField(max_length=32)
    allergies = models.CharField(max_length=100)
