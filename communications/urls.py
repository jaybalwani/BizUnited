from django.urls import path, include
from . import views
urlpatterns = [
    path('send/<str:pk>/', views.sendMessage, name = 'sendMessage'),
    path('inbox/', views.inbox, name = 'inbox'),
    path('inbox/<str:pk>/', views.message, name = 'single-message'),
]
