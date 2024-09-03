from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile, Entrepreneur,Investor


# Register your models here.

admin.site.register(Profile)
admin.site.register(Entrepreneur)
admin.site.register(Investor)