from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import WatchList
from startups.models import Pitch
from users.models import Investor

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    watchItems = WatchList.objects.filter(investor=request.user.profile.investor)
    return render(request, 'investors/dashboard.html', {'watchItems': watchItems})

@login_required(login_url='login')
def addWatchlistItem(request, pk):
    if request.user.profile.investor:
        watchListItem = WatchList.objects.create(
            pitch = Pitch.objects.get(id=pk),
            investor = Investor.objects.get(id=request.user.profile.investor.id)
    )
    return redirect('investor-dashboard')