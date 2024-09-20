from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='startup-dashboard'),
    path('pitches/', views.listPitches, name='startup-pitches'),
    path('add-pitch/', views.addPitch, name='add-pitch'),
]
