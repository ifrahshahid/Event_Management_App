from typing import List, Tuple
from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display: Tuple[str, ...] = ('title', 'date', 'location')
    search_fields: Tuple[str, ...] = ('title', 'description', 'location')
