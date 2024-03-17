from django.shortcuts import render

def index(request):
    return render(request, 'my_recipes/index.html')

# Create your views here.
