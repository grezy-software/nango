from __future__ import annotations

from importlib import import_module
from typing import TYPE_CHECKING

from django.apps import apps

from nango import cogs

if TYPE_CHECKING:
    from django.db import models


class CogsRunner:
    """Load and execute cogs.

    For the order execution, follow the nango.cogs.__all__ order.
    """

    model_filter_keywords: list[str] = ("django", "django_celery_beat", "rest_framework")

    def get_cogs_classes(self) -> list[callable]:
        """Return cogs's classes to execute."""
        return [getattr(import_module("nango.cogs"), cog_str) for cog_str in cogs.__all__]

    def get_settings_from_model(self, model: models.Model) -> dict[str, any]:
        """Return settings define in a model."""

    def _is_filtered_model(self, model: models.Model) -> bool:
        """Indicate if a model is filter or not.

        If the model is filter, we remove it.
        """
        return any(keyword in str(model) for keyword in self.model_filter_keywords)

    def run_cogs(self) -> None:
        """Run all existing cogs."""
        cogs_classes = self.get_cogs_classes()

        for model in apps.get_models():
            if self._is_filtered_model(model):
                return

            for cog in cogs_classes:
                instanciated_cog = cog(model=model, settings=self.get_settings_from_model(model))  # noqa: F841


if __name__ == "django.core.management.commands.shell":
    CogsRunner().run_cogs()
