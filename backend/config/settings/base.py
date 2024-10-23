"""Base settings to build other settings files upon."""

from pathlib import Path

import environ

CELERY_BROKER_URL = "redis://localhost:6379/0"

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent  # backend/
APPS_DIR = ROOT_DIR

# Setup env
env = environ.Env(
    DEBUG=(bool, False),
)
DEBUG = env.bool("DJANGO_DEBUG", False)
SECRET_KEY = env("DJANGO_SECRET_KEY")

# Stripe
STRIPE_PUBLISHABLE_KEY = env("STRIPE_PUBLISHABLE_KEY", default="")
STRIPE_SECRET_KEY = env("STRIPE_SECRET_KEY", default="")
STRIPE_ENDPOINT_SECRET = env("STRIPE_ENDPOINT_SECRET", default="")

# URLS
# ------------------------------------------------------------------------------
BASE_URL = "http://127.0.0.1:8000/"
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "config.urls"
# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "config.wsgi.application"

# Nango
FRONTEND_URL: str = env("FRONTEND_URL")
NANGO_TYPES_FOLDER: Path = ROOT_DIR / ".nango_front"
NANGO_TS_TYPES_FOLDER: Path = NANGO_TYPES_FOLDER / "ts_types"

if not NANGO_TYPES_FOLDER.exists():
    NANGO_TYPES_FOLDER.mkdir()
    NANGO_TS_TYPES_FOLDER.mkdir()
