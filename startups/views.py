from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Pitch

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'startups/dashboard.html')

@login_required(login_url='login')
def listPitches(request):
    pitches = Pitch.objects.all()
    context = {'pitches':pitches}
    return render(request, 'startups/list-pitches.html', context)