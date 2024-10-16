from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .utilities import searchQuery
from startups.models import Pitch

def home(request):
    if request.user.is_authenticated:
        if request.user.profile.role == 'ent':
            return render(request, 'startups/dashboard.html')
        elif request.user.profile.role == 'inv':
            return render(request, 'startups/dashboard.html')
    return render(request, 'index.html')

@login_required(login_url='login')
def userProfile(request):
    profile = request.user.profile
    context = {'profile': profile}
    return render(request, 'profile.html', context)

@login_required(login_url='login')
def globalPitches(request):
    query, pitches = searchQuery(request)
    context = {'pitches':pitches, 'query':query}
    return render(request, 'list-pitches.html', context)

@login_required(login_url='login')
def pitchDetailView(request, pk):
    pitch = Pitch.objects.get(id=pk)
    context = {'pitch':pitch}
    return render(request, 'detail-pitch.html', context)