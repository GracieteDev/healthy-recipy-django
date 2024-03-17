from django.views.generic import(
    CreateView, ListView, DetailView, UpdateView, DeleteView    
)  

from django.contrib.auth.mixins import (UserPassesTestMixin, LoginRequiredMixin)

from django.db.models import Q

from .models import Recipe
from.forms import RecipeForm


class Recipes(ListView):
    """
    View all recipes
    """ 
    model = Recipe
    template_name = 'recipes/index.html'
    context_object_name ='recipes'
    
    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        if query:
            recipes = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(instructions__icontains=query) |
                Q(cuisine_types__icontains=query)|
                Q(meal_type__icontains=query)
            )
        else:
            recipes = self.model.objects.all()
        return recipes
    

class AddRecipe(LoginRequiredMixin, CreateView):
    """
    Add a new recipe view 
    """
    model = Recipe
    form_class = RecipeForm
    success_url = '/recipes/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
class EditRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Edit a recipe
    """
    template_name = 'recipes/edit_recipe.html'
    model = Recipe
    form_class = RecipeForm
    success_url = '/recipes/'

    def test_func(self):
        return self.request.user == self.get_object().user
    
    
class RecipeDetail(DetailView):
    """
    Display a single recipe
    """
    model = Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'
    
class RecipeUpdate(UpdateView):
    """
    Update a recipe
    """
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_update.html'
    success_url = '/recipes/'


class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a recipe"""
    model = Recipe
    success_url = '/recipes/'

    def test_func(self):
        return self.request.user == self.get_object().user
    
    
    
    