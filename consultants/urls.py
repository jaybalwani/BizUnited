from django.urls import path
from . import views



urlpatterns = [
    path('', views.getConsultants, name="consultant-posts")
]
