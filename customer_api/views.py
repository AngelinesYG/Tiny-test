from django.shortcuts import render
from rest_framework import generics
from .serializers import CustomerSerializer
from .models import Customer
from .serializers import RecipesSerializer
from .models import Recipes
from .serializers import AllergensSerializer
from .models import Allergens

class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all().order_by('id')
    serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all().order_by('id')
    serializer_class = CustomerSerializer

#The below commented out code is the code I was trying for implementing the models for the data from the API. There is more description os this in the Readme file.
# class RecipesList(generics.ListCreateAPIView):
#     queryset = Recipes.objects.all().order_by('id')
#     serializer_class = RecipesSerializer
#
# class RecipesDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Recipes.objects.all().order_by('id')
#     serializer_class = RecipesSerializer
#
# class AllergensList(generics.ListCreateAPIView):
#     queryset = Allergens.objects.all().order_by('id')
#     serializer_class = AllergensSerializer
#
# class AllergensDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Allergens.objects.all().order_by('id')
#     serializer_class = AllergensSerializer
