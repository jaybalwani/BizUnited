from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='startup-dashboard'),
    path('add-pitch/', views.addPitch, name='add-pitch'),
]
