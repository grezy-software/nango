from django.db.models import fields as django_fields
from django.db.models.fields.reverse_related import ManyToOneRel, OneToOneRel

from nango.utils import AbstractCog


class SerializerCog(AbstractCog):
    """Generates a serializer from each django's models.

    Settings:
    --------
        - speedy (bool ; default = False): A faster serializer than rest_framework.serializers.Serializer, but with less features.
        - selected_fields (list[str] ; default = []): list of selected fields' name to serialize.
        - excluded_fields (list[str] ; default = []): list of fields' name to not serialize.
    """

    id = "serializer"

    # Fields to NEVER serialize.
    _forbidden_fields: tuple[str] = (
        "password",
        "outstandingtoken",
    )

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

    def get_model_fields(self) -> dict[str, django_fields.Field]:
        """Return the model fields to serialize.

        Returns:
        -------
        ```
        {
            "field_name": field,
            ...,
        }
        ```
        """
        selected_fields_name: list[str] = self.settings.get("selected_fields", [])
        if selected_fields_name:
            return {field_name: getattr(self.model, field_name) for field_name in selected_fields_name}

        model_fields_list: dict[str, django_fields.Field] = {}

        # Select all fields except excluded_fields
        excluded_fields_name: list[str] = self.settings.get("excluded_fields", [])
        for field in self.model._meta.get_fields():  # noqa: SLF001
            # Get field's name
            if isinstance(field, ManyToOneRel | OneToOneRel):
                # External Key point at actual model
                field_name = field.related_name if field.related_name is not None else f"{field.related_model.__name__.lower()}"
            else:
                field_name = getattr(field, "field_name", None) or getattr(field, "name", None)

            if field_name in excluded_fields_name or field_name in self._forbidden_fields:
                continue

            # Basic behavior
            model_fields_list[field_name] = field

        return model_fields_list

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
        self._get_model_fields()

        self.generate_cached_serializer()
        self.generated_customizable_serializer()
