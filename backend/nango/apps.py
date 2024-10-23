from django.apps import AppConfig
from django.db.models.signals import post_migrate


def create_nango_superuser(*args: list, **kwargs: dict) -> None:  # noqa: ARG001
    """Create a superuser at the 1st start of the db."""
    from django.conf import settings

    from nango.models import User

    password = getattr(settings, "SECRET_KEY", None)

    try:
        User.objects.get(username="Nango", email="contact@grezy.org")
    except User.DoesNotExist:
        User.objects.create_superuser(username="Nango", email="contact@grezy.org", password=password)
        print("Nango superuser has been created")  # noqa: T201


class NangoConfig(AppConfig):
    """."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "nango"
    verbose_name = "Nango"

    def ready(self) -> None:
        """Run the post-migrate for superuser creation."""
        post_migrate.connect(create_nango_superuser, sender=self)
