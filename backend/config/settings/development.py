import os

from config.settings.base import *  # noqa: F403
from config.settings.base import SECRET_KEY, env
from config.settings.modules import *  # noqa: F403
from config.settings.modules import REST_FRAMEWORK, SIMPLE_JWT

# Add signing key to JWT settings
SIMPLE_JWT["SIGNING_KEY"] = SECRET_KEY

# DOCKER
# ------------------------------------------------------------------------------
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
if env("USE_DOCKER") == "yes":
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]

# DJANGO
# ------------------------------------------------------------------------------
# https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#configuration
INSTALLED_APPS += ["django_extensions"]  # noqa: F405

REST_FRAMEWORK["DEFAULT_SCHEMA_CLASS"] = "drf_spectacular.openapi.AutoSchema"

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
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

# https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-DEFAULT_AUTO_FIELD
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1", "django"]  # noqa: S104
CORS_ALLOWED_ORIGINS = [f"http://{host}:3000" for host in ALLOWED_HOSTS]
CSRF_TRUSTED_ORIGINS = [f"http://{host}:3000" for host in ALLOWED_HOSTS]

# stop the reloader from going crazy
RUNSERVERPLUS_POLLER_RELOADER_TYPE = "stat"
