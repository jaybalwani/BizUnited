from django.db import models
from users.models import Investor
from startups.models import Pitch
import uuid

class WatchList(models.Model):
    pitch = models.ForeignKey(Pitch, on_delete=models.CASCADE)
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):  
        return self.pitch.title

