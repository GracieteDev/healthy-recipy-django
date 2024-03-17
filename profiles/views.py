from django.shortcuts import render, get_object_or_404
from .models import Profile

def profile_view(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    return render(request, 'profiles/profile.html', {'profile': profile})