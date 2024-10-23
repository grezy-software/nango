from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """."""

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: ClassVar = ["password"]

    email = models.EmailField(
        blank=False,
        null=False,
        unique=True,
        verbose_name="email address",
    )
    date_joined = None
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Date joined",
    )

    def __str__(self) -> str:
        """Display user."""
        return f"({self.id}) User: {self.email}"
