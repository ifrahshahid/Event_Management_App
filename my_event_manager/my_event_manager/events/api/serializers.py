# events/serializers.py

from rest_framework import serializers
from my_event_manager.events.models import Event
from my_event_manager.users.api.serializers import UserSerializer
from typing import Dict, Type

class EventSerializer(serializers.ModelSerializer):
    owner: UserSerializer = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model: Type[Event] = Event
        fields: tuple[str, ...] = '__all__'
        
