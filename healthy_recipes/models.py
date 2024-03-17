from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField
from cloudinary.models import CloudinaryField

# Choice Fields
MEAL_TYPES = (("breakfast", "Breakfast"), ("lunch", "Lunch"), ("dinner", "Dinner"))

CUISINE_TYPES = (
    ("african", "African"),
    ("american", "American"),
    ("caribbean", "Caribbean"),
    ("asian", "Asian"),
    ("middle_eastern", "Middle Eastern"),
    ("chinese", "Chinese"),
    ("indian", "Indian"),
    ("pakistani", "Pakistani"),
    ("indonesian", "Indonesian"),
    ("european", "European"),
    ("oceanic", "Oceanic"),
)

class Recipe(models.Model):
    """
    A model to create and manage recipes
    """

    user = models.ForeignKey(
        User, related_name="recipe_owner", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=300, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    instructions = RichTextField(max_length=10000, null=False, blank=False)
    ingredients = RichTextField(max_length=10000, null=False, blank=False)
    image = CloudinaryField('image')
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    
    #dropdown menus
    meal_type = models.CharField(max_length=50, choices=MEAL_TYPES, default="breakfast")
    cuisine_types = models.CharField(
        max_length=50, choices=CUISINE_TYPES, default="african"
    )
    servings = models.IntegerField(default=1, null=False, blank=False)
    posted_date = models.DateTimeField(
        auto_now=True)
    freezable = models.BooleanField(
        default=False)
    favourites = models.ManyToManyField(
        User, related_name='favourite', default=None, blank=True)
    

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ["-posted_date"]
