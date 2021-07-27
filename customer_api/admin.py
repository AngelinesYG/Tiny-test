from django.contrib import admin

from.models import Customer
from.models import Recipes
from.models import Allergens
admin.site.register(Customer)
admin.site.register(Recipes)
admin.site.register(Allergens)
