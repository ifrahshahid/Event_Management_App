from django.urls import path
from my_event_manager.events.api.views import EventViewSet

# Create an instance of EventViewSet
event_viewset = EventViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
event_detail_viewset = EventViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})
event_attend_viewset = EventViewSet.as_view({
    'post': 'attend',
})

app_name = 'events'
urlpatterns = [
    path('events/', event_viewset, name='event-list'),  # For GET list and POST create
    path('events/<int:pk>/', event_detail_viewset, name='event-detail'),  # For GET retrieve, PUT update, and DELETE destroy
    path('events/<int:pk>/attend/', event_attend_viewset, name='event-attend'),  # For POST attend
]
