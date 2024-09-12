from typing import ClassVar, Optional
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from .managers import UserManager

class User(AbstractUser):
    """
    Default custom user model for my_event_manager.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name: CharField = CharField(_("Name of User"), blank=True, max_length=255)
    first_name: None = None  # type: ignore[assignment]
    last_name: None = None  # type: ignore[assignment]
    email: EmailField = EmailField(_("email address"), unique=True)
    username: None = None  # type: ignore[assignment]
    mobile_number: Optional[CharField] = CharField(max_length=15, blank=True, null=True)

    USERNAME_FIELD: str = "email"
    REQUIRED_FIELDS: list[str] = []

    objects: ClassVar[UserManager] = UserManager()

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.
        """
        return reverse("users:detail", kwargs={"pk": self.id})
