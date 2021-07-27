
from django.urls import path
from . import views

urlpatterns = [
    path('', views.CustomerList.as_view(), name='customer_list'),
    path('api/customer/<int:pk>', views.CustomerDetail.as_view(), name='customer_detail'),

    # path('/recipes', views.RecipesList.as_view(), name='recipes_list'),
    # path('api/recipes/<int:pk>', views.RecipesDetail.as_view(), name='recipes_detail'),
    #
    # path('/recipes/allergens', views.AllergensList.as_view(), name='allergens_list'),
    # path('api/recipes/allergens<int:pk>', views.AllergensDetail.as_view(), name='allergens_detail')
]
