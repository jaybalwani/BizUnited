from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Pitch

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    pitches = Pitch.objects.filter(entrepreneur=request.user.profile.entrepreneur)
    print(pitches)
    context = {'pitches': pitches}
    return render(request, 'startups/dashboard.html', context)

@login_required(login_url='login')
def listPitches(request):
    pitches = Pitch.objects.all()
    context = {'pitches':pitches}
    return render(request, 'startups/list-pitches.html', context)

@login_required(login_url='login')
def addPitch(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        logo = request.FILES.get('image-startup')
        desc = request.POST.get('description')
        industry = request.POST.get('industry')
        stage = request.POST.get('stage')

        print (title, logo, desc, industry, stage)

        if None in (title, logo, desc, industry, stage):
            messages.error(request, 'Please fill out all the fields.')
            return redirect('add-pitch')
        
        pitch = Pitch.objects.create(
            entrepreneur=request.user.profile.entrepreneur,
            title=title,
            image=logo,
            description=desc,
            industry=industry,
            investment_stage=stage
        )
        pitch.save()
        return redirect('startup-dashboard')
    return render(request, 'startups/add-pitch.html')