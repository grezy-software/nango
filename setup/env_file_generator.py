"""Generate secrets for .django file of .env.

Run the script with the .env name as the first argument.
    backend/config/secret_generator.py <env_name>
"""  # noqa: INP001

import os
import sys
from pathlib import Path

from cryptography.fernet import Fernet


def _generate_key(multiplier: int = 1) -> str:
    """Generate a key with a multiplier."""
    key = "".join([Fernet.generate_key().decode()[:-1] for _ in range(multiplier)])
    while "\\" in key:
        key = "".join([Fernet.generate_key().decode()[:-1] for _ in range(multiplier)])
    return key


def get_or_generate_key(name: str, multiplier: int = 1) -> str:
    """Return the key if it exists, otherwise generate a new key."""
    result = os.environ.get(name, None)
    if result is None or result == "":
        result = _generate_key(multiplier)
    return result


def make_folder(env_name: str) -> Path:
    """Build .envs folder."""
    root_dir: Path = Path(__file__).resolve(strict=True).parent.parent.joinpath("backend")
    if not root_dir.is_dir():
        root_dir.mkdir(parents=True)
    folder = root_dir.joinpath(f".envs/.{env_name}")
    if not folder.is_dir():
        folder.mkdir(parents=True)
    return folder


def build_postgres_env(env_name: str) -> None:
    """Build .postgres file of .env."""
    folder: Path = make_folder(env_name)
    path: Path = folder.joinpath(".postgres")
    if path.exists():
        return

    content: str = f"""# PostgreSQL\n
# ------------------------------------------------------------------------------
POSTGRES_HOST = "postgres"
POSTGRES_PORT = 5432
POSTGRES_DB = "nango"
POSTGRES_USER = "nango"
POSTGRES_PASSWORD = "{get_or_generate_key(name="POSTGRES_PASSWORD", multiplier=2)}" # noqa: S105"""

    postgres_env_file = path.open("w+")
    postgres_env_file.writelines(content)
    postgres_env_file.close()


def build_django_secrets(env_name: str) -> None:
    """Build secrets for .django file of .env."""
    folder: Path = make_folder(env_name)
    path: Path = folder.joinpath(".django")

    if path.exists():
        return

    content: str = f"""# General\n
# ------------------------------------------------------------------------------
USE_DOCKER="yes"
IPYTHONDIR="/app/.ipython"
REDIS_URL="redis://redis:6379/0"
FRONTEND_URL="localhost:3000"
# Stripe
# ------------------------------------------------------------------------------
STRIPE_PUBLISHABLE_KEY = ""
STRIPE_SECRET_KEY = ""
STRIPE_ENDPOINT_SECRET = ""
# Django
# ------------------------------------------------------------------------------
DJANGO_SECRET_KEY="{get_or_generate_key(name="DJANGO_SECRET_KEY",  multiplier=2)}" # noqa: S105
DJANGO_DEBUG=True
IS_LOCAL=True
DJANGO_SETTINGS_MODULE="config.settings.{env_name}"
# Celery
CELERY_FLOWER_USER="{get_or_generate_key(name="CELERY_FLOWER_USER")}"
CELERY_FLOWER_PASSWORD="{get_or_generate_key(name="CELERY_FLOWER_PASSWORD", multiplier=2)}" # noqa: S105"""

    django_env_file = path.open("w+")
    django_env_file.writelines(content)
    django_env_file.close()


if __name__ == "__main__":
    env_name = sys.argv[1]
    build_postgres_env(env_name)
    build_django_secrets(env_name)
