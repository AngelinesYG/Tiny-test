from rest_framework import serializers
from .models import Customer
from .models import Recipes
from .models import Allergens

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'first_name','last_name', 'email', 'child_first_name', 'child_last_name', 'allergies',)

class RecipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = ('id', 'name', 'allergens', 'image_url')

class AllergensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergens
        fields = ('id', 'name')
