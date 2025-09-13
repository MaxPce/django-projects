from django.urls import path
from . import views

app_name = 'formapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('foods', views.create_food_item, name='new_food'),
    path('foods/<int:food_id>/delete', views.delete_food_item, name='delete_food'),
]