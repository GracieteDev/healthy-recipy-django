from django.shortcuts import render

def index(request):
    return render(request, 'healthy_recipes/index.html')