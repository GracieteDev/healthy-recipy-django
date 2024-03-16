from django.shortcuts import render
from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = 'home/index.html'

def my_recipes(request):
    # your view logic here...
    return render(request, 'my_recipes.html')

def healthy_recipes(request):
    # your view logic here...
    return render(request, 'healthy_recipes.html')

def add_recipe(request):
    # your view logic here...
    return render(request, 'add_recipe.html')
def profile(request,user_id):
    # your view logic here...
    return render(request, 'profile.html')