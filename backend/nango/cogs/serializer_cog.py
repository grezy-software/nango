from nango.utils import AbstractCog


class SerializerCog(AbstractCog):
    """Generates a serializer from each django's models.

    Settings:
    --------
        - speedy: A faster serializer than rest_framework.serializers.Serializer, but with less features.
    """

    id = "serializer"

    def _get_drf_imports(self) -> list[str]:
        """Return list of imports from rest_framework module."""
        if self.settings.get("speedy", False):
            error_msg: str = "The SerializerCog speedy feature is not implemented yet."
            raise NotImplementedError(error_msg)

        return [
            "from rest_framework import serializers" if not self.settings.get("speedy", False) else "...",
        ]

    def _get_base_imports(self) -> list[str]:
        """Return basics imports."""
        return [
            "from __future__ import annotations",
            "from typing import ClassVar",
        ]

    def get_serializer_name(self) -> dict[str]:
        """Return name of generated serializers.

        Returns:
        -------
        ```
        {
            "cached_serializer_name": str,
            "customizable_serializer_name": str,
        }
        ```
        """
        return {
            "cached_serializer_name": f"{self.model.__name__}NangoSerializer",
            "customizable_serializer_name": f"{self.model.__name__}Serializer",
        }

    def generate_cached_serializer(self) -> None:
        """Generate the serializer file (for the given model) that will be cached in the _nango_cache."""
        content: str = f"""
        {'\n'.join(self._get_base_imports())}
        {'\n'.join(self._get_drf_imports())}
        {self._get_model_import()}

        class {self.get_serializer_name().get('cached_serializer_name')}(serializer.Serializer):
            \"\"\"...generated...\"\"\"

            class Meta:
                model = {self.model.__name__}
        """
        print(content)  # noqa: T201

    def generated_customizable_serializer(self) -> None:
        """Generate the serializer file (for the given model) that use the cached serializer and that can be custom by the dev."""

    def run(self) -> None:
        """Generate a serializer for each django's model."""
        super().run()
        self.generate_cached_serializer()
        self.generated_customizable_serializer()
