from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from my_event_manager.users.api.views import UserViewSet
from my_event_manager.events.api.views import EventViewSet  

# Use DefaultRouter in debug mode for more features, SimpleRouter otherwise
router = DefaultRouter() if settings.DEBUG else SimpleRouter()

# Register viewsets with the router
router.register("users", UserViewSet)
router.register("events", EventViewSet)  

app_name = "api"
urlpatterns = router.urls
