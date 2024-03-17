from django.contrib import admin
from .models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title','user', 'instructions', 'ingredients', 'image', 'posted_date')

    list_filter = ('meal_type', 'cuisine_types')
    search_fields = ('title', 'description', 'ingredients', 'instructions')
    list_per_page = 20
    