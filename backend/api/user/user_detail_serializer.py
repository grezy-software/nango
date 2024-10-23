from typing import ClassVar

from api._nango_cache.user.user_detail_nango_serializer import User, UserDetailNangoSerializer


class UserDetailSerializer(UserDetailNangoSerializer):
    """Customizable serializer for User serializer."""

    class Meta:
        """."""

        model = User
        fields: ClassVar[list[str]] = [
            "id",
            "last_login",
            "is_superuser",
            "username",
            "first_name",
            "last_name",
            "is_staff",
            "is_active",
            "email",
            "created_at",
            "groups",
        ]
        read_only_fields: ClassVar[list[str]] = [
            "id",
            "last_login",
            "created_at",
            "is_superuser",
            "is_staff",
            "is_active",
            "groups",
        ]
