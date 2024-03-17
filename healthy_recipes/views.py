from django.shortcuts import render

def index(request):
    return render(request, 'healthy_recipes/index.html')

from django.shortcuts import render

def add_recipe(request):
    # Your view logic here...
    return render(request, 'healthy_recipes/add_recipe.html', context)