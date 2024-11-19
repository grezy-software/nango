from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from django.db import models


class AbstractCog(ABC):
    """Cog's base class, that gives the same basic functionalities for all cogs."""

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

    def is_executable(self) -> bool:
        """Indicate if the cog can run or not."""
        return self.settings is not None
