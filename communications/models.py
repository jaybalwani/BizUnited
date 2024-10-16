from django.db import models
from users.models import Profile
import uuid

class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True, related_name='messages')
    is_read = models.BooleanField(default=False, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.name
    
    ordering = ['-created']
