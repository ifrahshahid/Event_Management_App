from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from my_event_manager.events.models import Event
from .serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        else:
            return [IsAuthenticated()]
