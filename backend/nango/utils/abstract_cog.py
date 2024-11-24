from __future__ import annotations

import re
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from django.db import models


class AbstractCog(ABC):
    """Cog's base class, that gives the same basic functionalities for all cogs.

    If settings are not defined or is `{}`, the default settings will be used.
    Otherwise, if the settings are `None`, the Cog will not run.
    If one of the settings is not specified, the default value will be used.
    """

    id = None

    def __init__(self, model: models.Model, settings: dict[str, any]) -> None:
        """Setup the cogs.

        Elements of the setup:

            - Settings
        """
        self.model = model
        self.settings = settings.get(self.id, {})

    @abstractmethod
    def run(self) -> None:
        """Execute the cog logic."""
        if not self.is_executable():
            return

    def is_executable(self) -> bool:
        """Indicate if the cog can run or not."""
        return self.settings is not None

    def _generate_model_import(self) -> str:
        """Return the model import line for file generation."""
        regex = r"(?<=')(.*)(?=\.)"
        match = re.search(regex, str(self.model))
        import_path = match.group(1)

        return f"from {import_path} import {self.model.__name__}"
