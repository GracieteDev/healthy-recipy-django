# Generated by Django 3.2 on 2024-03-17 18:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=500)),
                ('instructions', djrichtextfield.models.RichTextField(max_length=10000)),
                ('ingredients', djrichtextfield.models.RichTextField(max_length=10000)),
                ('image', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=75, scale=None, size=[400, None], upload_to='recipes/')),
                ('image_alt', models.CharField(max_length=100)),
                ('meal_type', models.CharField(choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner')], default='breakfast', max_length=50)),
                ('cuisine_types', models.CharField(choices=[('african', 'African'), ('american', 'American'), ('caribbean', 'Caribbean'), ('asian', 'Asian'), ('middle_eastern', 'Middle Eastern'), ('chinese', 'Chinese'), ('indian', 'Indian'), ('pakistani', 'Pakistani'), ('indonesian', 'Indonesian'), ('european', 'European')], default='african', max_length=50)),
                ('calories', models.IntegerField(default=1)),
                ('servings', models.IntegerField(default=1)),
                ('posted_date', models.DateTimeField(auto_now=True)),
                ('freezable', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-posted_date'],
            },
        ),
    ]
