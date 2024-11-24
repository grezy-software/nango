from __future__ import annotations

from collections.abc import Callable
from importlib import import_module
from typing import TYPE_CHECKING

from django.apps import apps

from nango import cogs

if TYPE_CHECKING:
    from django.db import models


class CogsRunner:
    """Load and execute cogs.

    For the order execution, follow the nango.cogs.__all__ order.

    Settings:
    --------
    Nango's settings can be defined for each cog at the model level.
    A model can have a staticmethod called `nango` that returns a None (for no generation) or a dict (with settings for each cogs).
    """

    model_filter_keywords: list[str] = ("django", "django_celery_beat", "rest_framework")

    def get_cogs_classes(self) -> list[Callable]:
        """Return cogs's classes to execute."""
        return [getattr(import_module("nango.cogs"), cog_str) for cog_str in cogs.__all__]

    def get_settings_from_model(self, model: models.Model) -> dict[str, any]:
        """Return settings define in a model."""
        model_nango_method: Callable | None = getattr(model, "nango", None)
        if not isinstance(model_nango_method, Callable):
            if model_nango_method is None:
                # No settings defined in the model
                return {}
            error_msg: str = f"{model}.nango must be a staticmethod, not a property."
            raise TypeError(error_msg)
        return model_nango_method()

    def _is_filtered_model(self, model: models.Model) -> bool:
        """Indicate if a model is filter or not.

        If the model is filter, we don't run it.
        """
        return any(keyword in str(model) for keyword in self.model_filter_keywords)

    def run_cogs(self) -> None:
        """Run all existing cogs."""
        cogs_classes = self.get_cogs_classes()

        for model in apps.get_models():
            if self._is_filtered_model(model):
                continue
            for cog in cogs_classes:
                settings = self.get_settings_from_model(model)
                if settings is None:
                    # This model doesn't want any cogs.
                    continue

                # Run the cogs
                instantiated_cog = cog(model=model, settings=settings)
                instantiated_cog.run()


if __name__ == "django.core.management.commands.shell":
    CogsRunner().run_cogs()
