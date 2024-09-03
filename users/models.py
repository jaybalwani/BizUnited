from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Profile(models.Model):
    ROLE_VALUE = (
        ('inv', 'Investor'),
        ('ent', 'Entrepreneur'),
        ('con', 'Consultant')
        )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    role = models.CharField(max_length=200, choices=ROLE_VALUE)
    first_name = models.CharField(max_length=80, null=True, blank=True)
    last_name = models.CharField(max_length=80, null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='profile_pictures/', default='profile_pictures/default.jpg')
    bio = models.TextField(blank=True, null=True)
    socials_linkedin = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.username

class Entrepreneur(models.Model):
    STAGES = (
        ('none', 'None'),
        ('pre_seed', 'Pre-Seed'),
        ('seed', 'Seed'),
        ('series_a', 'Series A'),
        ('series_b', 'Series B'),
        ('series_c', 'Series C'),
        ('series_d', 'Series D'),
    )

    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    startup = models.CharField(max_length=100, null=True, blank=True)
    org_position = models.CharField(max_length=100, null=True, blank=True)
    industry = models.CharField(max_length=100, null=True, blank=True)
    education = models.CharField(max_length=100, null=True, blank=True)
    investment_stage =  models.CharField(max_length=200, choices=STAGES, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.profile.username

class Investor(models.Model):
    STAGES = (
        ('pre_seed', 'Pre-Seed'),
        ('seed', 'Seed'),
        ('series_a', 'Series A'),
        ('series_b', 'Series B'),
        ('series_c', 'Series C'),
        ('series_d', 'Series D'),
    )

    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    organization = models.CharField(max_length=100, null=True, blank=True)
    org_position = models.CharField(max_length=100, null=True, blank=True)
    preferred_stage =  models.CharField(max_length=200, choices=STAGES, null=True, blank=True)
    investment_focus = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)




    