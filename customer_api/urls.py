
from django.urls import path
from . import views

urlpatterns = [
    path('', views.CustomerList.as_view(), name='customer_list'),
    path('api/customer/<int:pk>', views.CustomerDetail.as_view(), name='customer_detail'),
]
