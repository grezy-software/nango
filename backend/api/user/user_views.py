from __future__ import annotations

from typing import TYPE_CHECKING

from nango.models.user import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .user_detail_serializer import UserDetailSerializer
from .user_serializer import UserSerializer

if TYPE_CHECKING:
    from typing import ClassVar

    from django.db.models import QuerySet
    from rest_framework.request import Request
    from rest_framework.serializers import Serializer


class UserView(GenericViewSet):
    """."""

    permission_classes: ClassVar[list] = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_permissions(self) -> list:
        """Return permission for the action."""
        match self.action:
            case "create":
                return []
            case _:
                return super().get_permissions()

    def get_serializer_class(self) -> Serializer:
        """Return the serializer for the action."""
        match self.action:
            case "create":
                return UserSerializer
            case "list" | "update" | "partial_update":
                return UserDetailSerializer
            case _:
                return super().get_serializer_class()

    def get_user(self) -> User:
        """Return the user for the action."""
        return self.request.user

    def get_queryset(self) -> QuerySet[User]:
        """Return the data for the action."""
        raise NotImplementedError
        return User.objects.all()

    def list(self, request: Request) -> Response:  # noqa: ARG002
        """Return User data."""
        queryset = self.get_user()
        serializer = self.get_serializer(queryset, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request: Request) -> Response:
        """Create a new User instance."""
        # Adjust username
        data = request.data
        username = data.get("username", data.get("email", "").split("@")[0])
        data["username"] = username

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request: Request, pk: int, **kwargs: dict[str, any]) -> Response:  # noqa: ARG002
        """Update a User instance."""
        user = self.get_user()

        # Adjust data
        data = request.data
        if data.get("username") is None:
            data["username"] = user.username
        if data.get("email") is None:
            data["email"] = user.email

        partial = kwargs.get("partial", False)
        serializer = self.get_serializer(user, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request: Request, pk: int) -> Response:
        """Partial update a User instance."""
        return self.update(request, pk, partial=True)

    def destroy(self, request: Request, pk: int) -> Response:  # noqa: ARG002
        """Delete a User instance."""
        instance = self.get_user()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
