"""CLI to run the Nango's bridge."""

from __future__ import annotations

import re
from importlib import import_module
from typing import TYPE_CHECKING

from api.urls import get_available_routes, main_api_router
from django.conf import settings
from django.core.management.base import BaseCommand, CommandParser
from rest_framework.serializers import Serializer

from nango.bridge import Bridge
from nango.bridge.type_factory import TsTypeFactory

if TYPE_CHECKING:
    from pathlib import Path


class Command(BaseCommand):
    """Cli to manage the bridge."""

    def add_arguments(self, parser: CommandParser) -> None:
        """."""
        # Positional arguments
        parser.add_argument("--force", "-f", action="store_true", help="Force the operation.")
        parser.add_argument("--types", "-t", action="store_true", help="Generate only types for frontend.")

        parser.add_argument("--routes", "-r", action="store_true")

    def display_available_routes(self, routes_data: dict) -> None:
        """Display available routes."""
        for module, routes in routes_data.items():
            print("\n", module)  # noqa: T201
            for route, methods in routes.items():
                print(f"\t└─ {route}")  # noqa: T201
                for method in methods:
                    print(f"\t\t└─ {method}")  # noqa: T201

    def _get_api_module_from_filepath(self, path: Path) -> str:
        """Transform a filepath into a python module to import.

        api/module/file -> api.module.file
        """
        return re.search("(api.*).py", str(path)).groups()[0].replace("/", ".")

    def get_all_serializers(self) -> list[Serializer]:
        """Parse object of api's folder to retrieve all serializers."""
        serializers_list: list[Serializer] = []
        api_folder_path: Path = settings.ROOT_DIR / "api"

        for filepath in api_folder_path.rglob("*"):
            if "serializer" not in filepath.name or not filepath.suffix.endswith(".py"):
                continue
            try:
                module = import_module(self._get_api_module_from_filepath(filepath))
            except ModuleNotFoundError:
                continue
            for obj in vars(module).values():
                if isinstance(obj, type) and issubclass(obj, Serializer) and obj != Serializer and "nango" not in obj.__module__.lower():
                    serializers_list.append(obj)  # noqa: PERF401

        return serializers_list

    def handle(self, *args: list, **options: dict) -> None:  # noqa: ARG002
        """Run the bridge."""
        if options["routes"]:
            routes_data: dict = get_available_routes(main_api_router)
            self.display_available_routes(routes_data)
            return

        bridge = Bridge(
            force=options.get("force", False),
        )
        bridge.clean()
        bridge.run()
        self.stdout.write(self.style.SUCCESS("All serializers and views have been created successfully!"))

        if options.get("types", False):
            ttf = TsTypeFactory()
            ttf.clean()
            ttf.generate_type_from_serializers(serializers=self.get_all_serializers())
            self.stdout.write(self.style.SUCCESS("All types have been generated successfully!"))
