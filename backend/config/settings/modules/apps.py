"""Installed apps."""

DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]


THIRD_PARTY_APPS = [
    "health_check",
    # Required
    "django_celery_beat",
    "corsheaders",
    "rest_framework",
    "rest_framework_api_key",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
]

LOCAL_APPS = [
    "nango",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
