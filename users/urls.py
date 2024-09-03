from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('onboarding/create-profile/', views.profileCreation, name='onboarding-profile'),
    path('onboarding/entrepreneur/', views.onboardingEnt, name='onboarding-entrepreneur'),
    path('onboarding/investor/', views.onboardingInv, name='onboarding-investor'),
]
