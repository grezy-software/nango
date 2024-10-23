from typing import ClassVar

from django.contrib.auth.password_validation import validate_password
from nango.models.user import User
from rest_framework.exceptions import ValidationError

from api._nango_cache.user.user_nango_serializer import UserNangoSerializer


class UserSerializer(UserNangoSerializer):
    """Customizable serializer for User serializer."""

    class Meta:  # noqa: D106
        model = User
        fields: ClassVar[list[str]] = [
            "id",
            "username",
            "first_name",
            "last_name",
            "is_active",
            "created_at",
            "email",
            # Write only fields
            "password",
        ]
        read_only_fields: ClassVar[list[str]] = [
            "id",
        ]
        extra_kwargs: ClassVar = {
            "password": {
                "write_only": True,
            },
        }

    def validate(self, data: dict) -> dict:
        """Validate user data."""
        password = data.get("password")
        email = data.get("email")
        if password is None or email is None:
            error_msg: str = "Password and email are mandatory for user creation"
            raise ValidationError(error_msg)

        validate_password(data.get("password"))
        return data

    def create(self, validate_data: dict) -> User:
        """."""
        user = User.objects.create_user(**validate_data)
        user.clean()
        return user
