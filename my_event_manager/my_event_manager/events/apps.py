# my_event_manager/events/apps.py

from django.apps import AppConfig

class EventsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_event_manager.events'

