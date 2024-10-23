from __future__ import annotations

import re
from typing import TYPE_CHECKING

import stripe
from django.conf import settings
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

if TYPE_CHECKING:
    from typing import ClassVar

    from nango.models.user import User
    from rest_framework.authentication import BaseAuthentication
    from rest_framework.request import Request


class StripeView(GenericViewSet):
    """."""

    permission_classes: ClassVar[list] = [IsAuthenticated]

    def get_user(self) -> User:
        """Return the user for the action."""
        return self.request.user

    def get_permissions(self) -> list:
        """Return permission for the action."""
        match self.action:
            case "webhook":
                return [AllowAny()]
            case _:
                return super().get_permissions()

    def get_authenticators(self) -> BaseAuthentication:
        """Return authenticators for the action."""
        if self.request.build_absolute_uri().endswith("webhook/"):
            return []
        return super().get_authenticators()

    @staticmethod
    def get_base_api_url(request: Request) -> str:
        """Return base url."""
        base_url = settings.FRONTEND_URL
        if base_url is not None:
            return base_url
        regex = r"(http.?:\/\/.+?\/)"
        return re.findall(regex, request.build_absolute_uri())[0]

    @action(detail=False, methods=["get"])
    def checkout_session(self, request: Request) -> Response:
        """Create stripe checkout session."""
        stripe.api_key = settings.STRIPE_SECRET_KEY
        base_api_url = self.get_base_api_url(request)
        try:
            # Inline stripe payment.
            checkout_session = stripe.checkout.Session.create(
                success_url=base_api_url + "?success=True",
                cancel_url=base_api_url + "?success=False",
                customer_email=self.get_user().email,
                payment_method_types=["card"],
                mode="payment",
                line_items=[...],
            )
            checkout_session_id = checkout_session["id"]  # noqa: F841
            # Logic on database object

            return Response({"sessionUrl": checkout_session["url"]}, status=status.HTTP_200_OK)
        except Exception:  # noqa: BLE001
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=["post"])
    def webhook(self, request: Request) -> Response:
        """Stripe webhook."""
        stripe.api_key = settings.STRIPE_SECRET_KEY
        endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
        event = None
        payload = request.body
        sig_header = request.headers["STRIPE_SIGNATURE"]
        try:
            event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
        except ValueError:
            return Response({"error": "ValueError"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except stripe.error.SignatureVerificationError:
            return Response({"error": "Stripe Signature Verification Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Handle the event
        if event["type"] == "checkout.session.completed":
            session_id = event["data"]["object"]["id"]  # noqa: F841
            # Logic on database object

            print("Payment was successful.")  # noqa: T201
        elif "failed" in event["type"]:
            print(f"Failed operation: {event["type"]}")  # noqa: T201
        else:
            print(f"Unhandled event type {event["type"]}")  # noqa: T201

        return Response(status=status.HTTP_200_OK)
