from django.contrib import admin
from .models import Recipe

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'meal_type', 'instructions', 'ingredients', 'image', 'posted_date')
    list_filter = ('meal_type',)
    search_fields = ('title', 'meal_type', 'description', 'ingredients', 'instructions',)
    list_per_page = 6