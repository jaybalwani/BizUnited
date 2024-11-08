"""
URL configuration for bizunited project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
import users.urls as user_urls
import startups.urls as startup_urls
import investors.urls as investor_urls
import communications.urls as messaging_urls
import consultants.urls as consultant_urls
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('users/', include(user_urls)),
    path('startups/', include(startup_urls)),
    path('investors/', include(investor_urls)),
    path('messaging/', include(messaging_urls)),
    path('consult/', include(consultant_urls )),
    path('profile/', views.userProfile, name='user-profile'),
    path('pitches/', views.globalPitches, name='global-pitches'),
    path('pitch/<str:pk>/', views.pitchDetailView, name='single-pitch'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
