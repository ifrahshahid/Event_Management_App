

from django.db import models
from django.utils import timezone
from django.conf import settings

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.title
