from django.db import models
# from django.contrib.postgres.fields import EmailField

class Customer(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(max_length=40)
    child_first_name = models.CharField(max_length=32)
    child_last_name = models.CharField(max_length=32)
    allergies = models.CharField(max_length=100)

class Recipes(models.Model):
    name = models.CharField(max_length=40, blank = True, null = True)
    allergens = models.CharField(max_length=100, blank = True, null = True)
    image_url = models.CharField(max_length=100, blank = True, null = True)

class Allergens(models.Model):
    name = models.CharField(max_length=40, blank = True, null = True)
