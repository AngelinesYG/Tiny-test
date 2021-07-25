from rest_framework import serializers
from .models import Contact

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'first_name','last_name', 'email', 'child_first_name', 'child_last_name', 'allergies',)
