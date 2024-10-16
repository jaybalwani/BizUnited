from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='investor-dashboard'),
    path('watchlist/<str:pk>', views.addWatchlistItem, name='add-watchlist-item'),
]
