from django.shortcuts import render

def home(request):
    if request.user.is_authenticated:
        if request.user.profile.role == 'ent':
            return render(request, 'startups/dashboard.html')
        elif request.user.profile.role == 'inv':
            return render(request, 'startups/dashboard.html')
    return render(request, 'index.html')