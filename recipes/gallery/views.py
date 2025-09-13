from django.shortcuts import render
from .models import Recipe
# Create your views here.
def index(request):
    recipe_list = Recipe.objects.all()
    context = {'recipes': recipe_list}
    return render(request, 'gallery/index.html',context)