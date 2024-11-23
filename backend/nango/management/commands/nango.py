"""CLI to run the Nango's bridge."""

from __future__ import annotations

from django.core.management.base import BaseCommand, CommandParser


class Command(BaseCommand):
    """Cli to manage the bridge."""

    def add_arguments(self, parser: CommandParser) -> None:
        """."""

    def handle(self, *args: list, **options: dict) -> None:
        """Handle argument and run Nango's cogs."""
