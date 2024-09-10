# events/serializers.py

from rest_framework import serializers
from my_event_manager.events.models import Event
from my_event_manager.users.api.serializers import UserSerializer

class EventSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True) 
    
    class Meta:
        model = Event
        fields = '__all__'
