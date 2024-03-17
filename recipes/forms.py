from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Recipe

class RecipeForm( forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "title",
            "description",
            "ingredients",
            "instructions",
            "image",
            "image_alt",
            "meal_type",
            "cuisine_types",
            "calories",
            "servings",
            ]
        widgets = {
            'description':forms.Textarea(attrs={"rows": 5}),
        }
        labels = {
            'title': 'Recipe Title',
            'description': 'Description',
            'meal_type': 'Meal Type',
            'cuisine_types': 'Cuisine Types',
            'ingredients': 'Ingredients',
            'instructions': 'Instructions',
            'image': 'Image',
            "image_alt": "Describe Image",
            "meal_type": "Meal Type",
            "cuisine_types": "Cuisine Type",
            "calories": "Calories",
        }
        help_texts = {
            'title': 'Enter the title of the recipe',
            'description': 'Enter a brief description of the recipe',
            'meal_type': 'Select the meal type of the recipe',
            'cuisine_types': 'Select the cuisine type of the recipe',
            'ingredients': 'Enter the ingredients of the recipe',
            'instructions': 'Enter the instructions of the recipe',
            'image': 'Upload an image of the recipe',
        }
        error_messages = {
            'title': {
                'max_length': "This title is too long.",
            },
        }
        field_classes = {
            'title': forms.CharField,
            'description': forms.CharField,
            'meal_type': forms.CharField,
            'cuisine_types': forms.CharField,
            'ingredients': forms.CharField,
            'instructions': forms.CharField,
            'image': forms.ImageField,
        }
        required = {
            'title': True,
            'description': True,
            'meal_type': True,
            'cuisine_types': True,
            'ingredients': True,
            'instructions': True,
            'image': True,
        }
        help_texts = {
            'title': 'Enter the title of the recipe',
            'description': 'Enter a brief description of the recipe',
            'meal_type': 'Select the meal type of the recipe',
            'cuisine_types': 'Select the cuisine type of the recipe',
            'ingredients': 'Enter the ingredients of the recipe',
            'instructions': 'Enter the instructions of the recipe',
            'image': 'Upload an image of the recipe',
        }
        
        initial = {
            'title': 'Enter the title of the recipe',
            'description': 'Enter a brief description of the recipe',
            'meal_type': 'Select the meal type of the recipe',
            'cuisine_types': 'Select the cuisine type of the recipe',
            'ingredients': 'Enter the ingredients of the recipe',
            'instructions': 'Enter the instructions of the recipe',
            'image': 'Upload an image of the recipe',
        }
        