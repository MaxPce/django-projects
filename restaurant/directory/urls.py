from django.urls import path
from . import views

app_name = 'restaurant'
urlpatterns = [
    path('', views.index, name='index'),
    path('restaurants/', views.restaurant_detail, name='restaurant_detail'),
    path('chefs/', views.chef_detail, name='chef_detail'),
    path('foods/', views.food_detail, name='food_detail'),
]