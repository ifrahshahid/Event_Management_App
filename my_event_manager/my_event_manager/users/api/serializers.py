from typing import Dict, Type
from rest_framework import serializers
from my_event_manager.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model: Type[User] = User
        fields: tuple[str, ...] = ("name", "email", "mobile_number", "url")
        
        extra_kwargs: Dict[str, Dict[str, str]] = {
            "url": {"view_name": "api:user-detail", "lookup_field": "pk"},
        }
