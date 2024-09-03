from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile,Entrepreneur,Investor
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect('startup-dashboard')

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)            
        except:
            messages.error(request, 'User does not exist.')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            if user.profile.role == 'inv':
                return redirect('investor-dashboard')
            elif user.profile.role == 'ent':
                return redirect('startup-dashboard')
        else:
            messages.error(request, 'User OR Password incorrect.')
    return render(request, 'users/login.html')

@login_required
def logout(request):
    auth_logout(request)
    messages.success(request, 'User logged out.')
    return redirect('home')

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        if not username or not password or not email:
            messages.error(request, 'Please fill all the fields.')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'User already exists.')
            return redirect('register')

        user = User.objects.create_user(username, email, password)
        user.save()

        auth_login(request, user)
        return redirect('onboarding-profile')

    return render(request, 'users/register.html')

@login_required(login_url='login')
def profileCreation(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        bio = request.POST.get('bio')
        linkedin = request.POST.get('socials_linkedin')
        role = request.POST.get('role')
        profile_pic = request.POST.get('profile_pic')

        if Profile.objects.filter(user = request.user).exists():
            return redirect('home')
        
        profile = Profile.objects.create(
            user = request.user,        
            first_name = fname,
            last_name = lname,
            bio = bio,
            socials_linkedin = linkedin,
            profile_pic = profile_pic,
            role = role,
            username = request.user.username,
            email = request.user.email
        )

        profile.save()

        if role == 'ent':
            return redirect('onboarding-entrepreneur')
        elif role == 'inv':
            return redirect('onboarding-investor')
        
    return render(request, 'users/profile_role.html')

@login_required(login_url='login')
def onboardingEnt(request):

    if request.method == 'POST':
        education = request.POST.get('education')
        indsutry = request.POST.get('industry')
        organization = request.POST.get('organization')
        position = request.POST.get('position')
        stage = request.POST.get('stage')
        location = request.POST.get('location')

        if Entrepreneur.objects.filter(profile = request.user.profile).exists():
            return redirect('home')
        
        ent = Entrepreneur.objects.create(
            profile=request.user.profile,
            startup=organization,
            org_position=position,
            industry=indsutry,
            education=education,
            location=location,
            investment_stage = stage
        )

        ent.save()
        return redirect('startup-dashboard')

    return render(request, 'users/onboarding-ent.html')

@login_required
def onboardingInv(request):
    if request.method == 'POST':
        if Investor.objects.filter(profile = request.user.profile).exists():
            return redirect('home')
        
        stage = request.POST.get('stage')
        focus = request.POST.get('focus')
        org = request.POST.get('org')
        position = request.POST.get('position')
        
        inv = Investor.objects.create(
            profile=request.user.profile,
            organization=org,
            org_position=position,
            preferred_stage=stage,
            investment_focus=focus
        )

        inv.save()
        return redirect('investor-dashboard')

    return render(request, 'users/onboarding-inv.html')