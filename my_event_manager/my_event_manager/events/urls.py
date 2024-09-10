from django.urls import path, include
from rest_framework.routers import DefaultRouter
from my_event_manager.events.api.views import EventViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
