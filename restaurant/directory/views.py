from django.shortcuts import render
from .models import Restaurant, Place, Food, Chef
# Create your views here.

def index(request):
    places = Place.objects.all()
    context = {
        'places': places,
    }
    return render(request, 'restaurant/index.html', context)

def restaurant_detail(request):
    places = Place.objects.all()
    get_restaurant = request.GET.get('restaurant')
    restaurant = Restaurant.objects.filter(place__name=get_restaurant)
    print(get_restaurant)
    context = {
        'places': places,
        'restaurants': restaurant,
        'list_restaurants': len(restaurant),
    }
    return render(request, 'restaurant/restaurant.html', context)

def chef_detail(request):
    get_chef = request.GET.get('chef')
    chef = Chef.objects.filter(name=get_chef)
    places = Place.objects.all()
    context = {
        'places': places,
        'chefs': chef,
        'list_chefs': len(chef),
    }
    return render(request, 'restaurant/chef.html', context)

def food_detail(request):
    get_food = request.GET.get('food')
    food = Food.objects.filter(name=get_food)
    places = Place.objects.all()
    context = {
        'places': places,
        'foods': food,
        'list_foods': len(food),
    }
    return render(request, 'restaurant/food.html', context)