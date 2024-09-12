

from typing import Type
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class Event(models.Model):
    title: str = models.CharField(max_length=200)
    description: str = models.TextField()
    date: models.DateTimeField = models.DateTimeField(default=timezone.now)
    location: str = models.CharField(max_length=255)
    owner: models.ForeignKey = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    attendees: models.ManyToManyField = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='attended_events', blank=True)
    
    def __str__(self) -> str:
        return self.title
