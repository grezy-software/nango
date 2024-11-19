from nango.utils.abstract_cog import AbstractCog

__all__ = [
    "AbstractCog",
]


def setup_django() -> None:
    """Setup django environment."""
    import os
    import sys
    from pathlib import Path

    path = Path(__file__).parent.parent
    sys.path.append(str(path))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", os.environ.get("DJANGO_SETTINGS_MODULE", "config.settings.development"))
    import django

    django.setup()
