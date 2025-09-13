from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .models import FoodItem
# Create your views here.

def index(request):
    list_foods = FoodItem.objects.all()
    context = {
        'list_foods': list_foods
    }
    return render(request, 'formapp/index.html',context)

def create_food_item(request):
    total_calories = (float(request.POST['carbohydrates'])* 4 + float(request.POST['protein'])* 4 + float(request.POST['fat'])* 9)
    new_food = FoodItem(
        name=request.POST.get('name'),
        calories=total_calories,
        protein=request.POST.get('protein'),
        fat=request.POST.get('fat'),
        carbohydrates=request.POST.get('carbohydrates'),
        date=request.POST.get('date')
    )
    new_food.save()
    return HttpResponseRedirect(reverse('formapp:index'))

def delete_food_item(request, food_id):
    try:
        food_item = FoodItem.objects.get(id=food_id)
        food_item.delete()
        return HttpResponseRedirect(reverse('formapp:index'))
    except FoodItem.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Food item not found'}, status=404)

