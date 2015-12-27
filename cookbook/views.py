from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse

from cookbook.models import Category, Recipe, Ingredient
from .filters import RecipeFilter

def index(request):
    category_list = Category.objects.order_by('-name')
    context_dict = {'categories': category_list}
    return render(request, 'cookbook/index.html', context_dict)


def category(request, category_name_slug):
    context_dict = {}

    category = get_object_or_404(Category, slug=category_name_slug)
    context_dict['category_name'] = category.name

    recipes = Recipe.objects.filter(category=category)
    context_dict['recipes'] = recipes
    context_dict['category'] = category

    return render(request, 'cookbook/category.html', context_dict)


def recipe(request, recipe_name_slug):
    context_dict = {}
    recipe = get_object_or_404(Recipe, slug=recipe_name_slug)
    context_dict['recipe'] = recipe
    ingredients = Ingredient.objects.filter(recipe=recipe).order_by('place')
    context_dict['ingredients'] = ingredients

    return render(request, 'cookbook/recipe.html', context_dict)


def recipe_list(request):
    f = RecipeFilter(request.GET, queryset=Recipe.objects.all().order_by('book_page'))
    return render_to_response('cookbook/recipelist.html', {'filter': f})