from django.db import models
from users.models import Entrepreneur
import uuid

# Create your models here.

class Pitch(models.Model):
    STAGES = (
        ('none', 'None'),
        ('pre_seed', 'Pre-Seed'),
        ('seed', 'Seed'),
        ('series_a', 'Series A'),
        ('series_b', 'Series B'),
        ('series_c', 'Series C'),
        ('series_d', 'Series D'),
    )

    entrepreneur = models.ForeignKey(Entrepreneur, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='pitch_images/', default='', null=True, blank=True)
    investment_stage = models.CharField(max_length=50, null=True, blank=True, choices=STAGES)
    industry = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):  
        return self.title
