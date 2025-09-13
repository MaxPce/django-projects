from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import models
import json

# Create your views here.

def index(request):
    all_recipes = models.Recipes.objects.all()
    recipes_json = []
    for recipe in all_recipes:
        new_recipe = {
            'id': recipe.id,
            'title': recipe.title,
            'ingredients': recipe.ingredients,
            'preparation': recipe.preparation,
            'people': recipe.people,
            'onMenu': recipe.onMenu,
        }
        recipes_json.append(new_recipe)
    return JsonResponse(recipes_json, safe=False, json_dumps_params={'ensure_ascii': False})
def get_one_recipe(request, recipe_id):
    try:
        recipe = models.Recipes.objects.get(id=recipe_id)
        recipe_json = {
            'id': recipe.id,
            'title': recipe.title,
            'ingredients': recipe.ingredients,
            'preparation': recipe.preparation,
            'people': recipe.people,
            'onMenu': recipe.onMenu,
        }
        return JsonResponse(recipe_json, json_dumps_params={'ensure_ascii': False})
    except models.Recipes.DoesNotExist:
        return JsonResponse({'error': 'Recipe not found'}, status=404)