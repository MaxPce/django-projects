from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:recipe_id>/', views.get_one_recipe, name='get_one_recipe'),
]