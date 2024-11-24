from __future__ import annotations

from collections.abc import Callable
from importlib import import_module
from typing import TYPE_CHECKING

from django.apps import apps
from django.conf import settings

from nango import cogs

if TYPE_CHECKING:
    from django.db import models


class CogsRunner:
    """Load and execute cogs.

    For execution order, follow the nango.cogs.__all__ order.

    Settings:
    --------
    Nango's settings can be defined for each cog at the model level.
    A model can have a staticmethod called `nango` that returns a None (for no generation) or a dict (with settings for each cogs).
    """

    def get_cog_classes(self) -> list[Callable]:
        """Return cogs's classes to execute."""
        return [getattr(import_module("nango.cogs"), cog_str) for cog_str in cogs.__all__]

    def get_local_model_classes(self) -> list[models.Model]:
        """Get all models for apps defined in settings.LOCAL_APPS."""
        model_list: list[models.Model] = []

        for app_name in settings.LOCAL_APPS:
            app_config = apps.app_configs.get(app_name)
            model_list.extend(app_config.get_models())
        return model_list

    def get_settings_from_model(self, model: models.Model) -> dict[str, any]:
        """Return settings defined in a model."""
        model_nango_method: Callable | None = getattr(model, "nango", None)

        if not isinstance(model_nango_method, Callable):
            if model_nango_method is None:
                # No settings defined in the model
                return {}

            error_msg: str = f"{model}.nango must be a staticmethod, not a property."
            raise TypeError(error_msg)

        return model_nango_method()

    def run_cogs(self) -> None:
        """Run all existing cogs."""
        cogs_classes = self.get_cogs_classes()

        for model in self.get_local_model_classes():
            for cog in cogs_classes:
                model_nango_settings = self.get_settings_from_model(model)

                # This model doesn't want any cogs.
                if model_nango_settings is None:
                    continue

                # Run the cogs
                instantiated_cog = cog(model=model, settings=model_nango_settings)
                instantiated_cog.run()
