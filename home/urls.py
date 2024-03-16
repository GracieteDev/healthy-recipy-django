from django.urls import path
from .views import Index, my_recipes, healthy_recipes, add_recipe, profile

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('my_recipes/', my_recipes, name='my_recipes'),
    path('healthy_recipes/', healthy_recipes, name='healthy_recipes'),
    path('add_recipe/', add_recipe, name='add_recipe'),
    path('profile/<int:user_id>', profile, name='profile'),
    # other url patterns...
]