"""CLI to run the Nango's bridge."""

from __future__ import annotations

from django.core.management.base import BaseCommand, CommandParser

from nango.utils import CogsRunner


class Command(BaseCommand):
    """Cli to manage the bridge."""

    def add_arguments(self, parser: CommandParser) -> None:
        """."""

    def handle(self, *args: list, **options: dict) -> None:  # noqa: ARG002
        """Handle argument and run Nango's cogs."""
        CogsRunner().run_cogs()
