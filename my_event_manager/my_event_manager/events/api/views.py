from typing import List, Type
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import action
from rest_framework.response import Response
from my_event_manager.events.models import Event
from .serializers import EventSerializer
from rest_framework.request import Request

class EventViewSet(viewsets.ModelViewSet):
    queryset: Type[Event] = Event.objects.select_related('owner').all()
    serializer_class: Type[EventSerializer] = EventSerializer

    def get_permissions(self) -> List[IsAuthenticated | AllowAny]:
        if self.action == 'list':
            return [AllowAny()]
        return [IsAuthenticated()]

    def perform_create(self, serializer: EventSerializer) -> None:
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer: EventSerializer) -> None:
        event: Event = self.get_object()
        if event.owner != self.request.user:
            raise PermissionDenied("You do not have permissions to update this event.")
        serializer.save()

    def perform_destroy(self, instance: Event) -> None:
        if instance.owner != self.request.user:
            raise PermissionDenied("You do not have permissions to delete this event.")
        instance.delete()

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def attend(self, request: Request, pk: int = None) -> Response:
        event: Event = self.get_object()
        user = request.user
        
        if user in event.attendees.all():
            return Response({"detail": "You are already attending this event."}, status=status.HTTP_400_BAD_REQUEST)
        
        event.attendees.add(user)
        return Response({"detail": "Successfully marked as attending."}, status=status.HTTP_200_OK)
