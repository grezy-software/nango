import os

from django.db.backends.signals import connection_created
from django.dispatch import receiver

from config.settings.base import *  # noqa: F403
from config.settings.base import ROOT_DIR, SECRET_KEY, env
from config.settings.modules import *  # noqa: F403
from config.settings.modules import SIMPLE_JWT

# Add signing key to JWT settings
SIMPLE_JWT["SIGNING_KEY"] = SECRET_KEY

# Use merged .envs
env.read_env(str(ROOT_DIR / ".env"))

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT"),
    },
}

DATABASES["default"]["ATOMIC_REQUESTS"] = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


ALLOWED_HOSTS = ["django", "localhost"]


@receiver(connection_created)
def set_busy_timeout(sender, connection, **kwargs):  # noqa
    if connection.vendor == "sqlite":
        cursor = connection.cursor()
        cursor.execute("PRAGMA busy_timeout = 5000;")


connection_created.connect(set_busy_timeout)

CORS_ALLOWED_ORIGINS = [f"http://{host} " for host in ALLOWED_HOSTS] + [f"https://{host} " for host in ALLOWED_HOSTS]
CSRF_TRUSTED_ORIGINS = CORS_ALLOWED_ORIGINS.copy()
