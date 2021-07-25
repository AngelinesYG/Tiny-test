from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)
    child_first_name = models.CharField(max_length=32)
    child_last_name = models.CharField(max_length=32)
    allergies = models.CharField(max_length=100)
