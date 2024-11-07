from __future__ import annotations

import shutil
from typing import TYPE_CHECKING

from django.conf import settings
from jinja2 import Environment, FileSystemLoader
from rest_framework.fields import Field, ListField
from rest_framework.relations import ManyRelatedField, PrimaryKeyRelatedField
from rest_framework.serializers import ListSerializer, Serializer

from nango.bridge.float_serializer_method_field import FloatSerializerMethodField
from nango.bridge.string_serializer_method_field import StringSerializerMethodField

if TYPE_CHECKING:
    from pathlib import Path


class AbstractTypeFactory:
    """Abstract classes for type generator.

    A type is always generated from a serializer.
    """

    def __init__(self, **kwargs: dict[str, any]) -> None:
        """."""
        # Jinja
        self._template_folderpath: Path = settings.ROOT_DIR / "nango/templates"
        self._jinja_env = Environment(
            loader=FileSystemLoader(self._template_folderpath),
            autoescape=True,
        )
        self.template_name = getattr(self, "template_name", None) or kwargs.get("template_name")
        if self.template_name is None:
            error_msg: str = "Your child class must specify an template_name."
            raise ValueError(error_msg)
        if not self._template_folderpath.joinpath(self.template_name).exists():
            error_msg: str = f"Path {self._template_folderpath.joinpath(self.template_name)} does not exist."
            raise ValueError(error_msg)

    def get_type_name(self, serializer: Serializer | ListSerializer) -> str:
        """Return the type name, deduced from the serializer's name."""
        if isinstance(serializer, ListSerializer | ListField):
            return self.get_type_name(serializer.child)

        match serializer.__class__.__name__:
            case "BooleanField":
                return "boolean"
            case "CharField" | "EmailField" | "ChoiceField":
                return "string"
            case "DateField" | "DateTimeField":
                return "string"
            case "IntegerField" | "FloatField":
                return "number"
        return serializer.__class__.__name__.split("Serializer")[0]

    def get_generated_filepath(self, serializer: Serializer) -> Path:
        """Return the path of the generated file for the given serializer."""
        folder_path: Path = settings.NANGO_TS_TYPES_FOLDER
        return folder_path / f"{self.get_type_name(serializer)}.ts"

    def get_type_imports(self, serializer: Serializer) -> list[str]:
        """Return the imports of other generated serializer to import."""
        return [
            self.get_type_name(field)
            for field in serializer.fields.values()
            if isinstance(field, Serializer | ListSerializer)
            if self.get_type_name(field)
            not in [
                "boolean",
                "string",
                "Date",
                "number",
            ]
        ]

    def map_serializer_field_to_type(self, field: Field) -> str:
        """Return the type of the given type."""
        raise NotImplementedError

    def convert_serializer_to_type(self, serializer: Serializer) -> dict[str, str]:
        """Convert a serializer to frontend Type."""
        if not isinstance(serializer, Serializer):
            error_msg: str = f"serializer must be a '{type(Serializer)}' instance (type of {serializer} is '{type(serializer)}')."
            raise TypeError(error_msg)

        data: dict[str, str] = {}
        for name, field in serializer.fields.items():
            ts_type: str = self.map_serializer_field_to_type(field)
            if ts_type:
                data[name] = ts_type

        return data

    def generate_type(self, target_filepath: str, data: dict, *, mode: str = "w") -> None:
        """Generate type file.

        Args:
        ----
            target_filepath (str): Path of the generated file.
            data (dict): Data used to generate the file.
            mode (str): Mode used for file opening.
        """
        # Render jinja template
        template = self._jinja_env.get_template(self.template_name)
        content = template.render(data)

        # Write content into target file
        target_file = target_filepath.open(mode=mode)
        target_file.write(content)
        target_file.close()

    def generate_type_from_serializers(self, serializers: list[Serializer]) -> None:
        """Convert a list of serializers into frontend Type and generate file and generate file."""
        if not isinstance(serializers, list):
            error_msg: str = "Please give a list of Serializers"
            return TypeError(error_msg)

        for serializer in serializers:
            instantiated_serializer = serializer()
            ts_type = self.convert_serializer_to_type(instantiated_serializer)
            generated_filepath = self.get_generated_filepath(instantiated_serializer)
            self.generate_type(
                target_filepath=generated_filepath,
                data={
                    "type_name": self.get_type_name(instantiated_serializer),
                    "fields": ts_type,
                    "imports": self.get_type_imports(instantiated_serializer),
                },
            )

        return None


class TsTypeFactory(AbstractTypeFactory):
    """Generate TsType instances."""

    def __init__(self, **kwargs: dict[str, any]) -> None:
        """."""
        self.template_name = "ts_type.j2"
        super().__init__(**kwargs)

    def map_serializer_field_to_type(self, field: Field) -> str:  # noqa: PLR0911
        """Return the type of the given type."""
        if not isinstance(field, Field):
            error_msg: str = f"field must be a 'rest_framework.fields.Field' instance (currently: '{type(field)}')."
            raise TypeError(error_msg)

        match field.__class__.__name__:
            case "BooleanField":
                return "boolean"
            case "CharField" | "EmailField" | "ChoiceField":
                return "string"
            case "DateField" | "DateTimeField":
                return "string"
            case "IntegerField" | "FloatField":
                return "number"

        if isinstance(field, PrimaryKeyRelatedField):
            return "number"
        if isinstance(field, Serializer):
            return f"{self.get_type_name(field)}"
        if isinstance(field, ManyRelatedField):
            return "number[]"
        if isinstance(field, ListSerializer | ListField):
            return f"{self.get_type_name(field)}[]"
        if isinstance(field, StringSerializerMethodField):
            return "string"
        if isinstance(field, FloatSerializerMethodField):
            return "number"
        print(f"Impossible to get a TypeScript match for {field} ({type(field)})")  # noqa: T201
        return ""

    def clean(self) -> None:
        """Clean the TS types folder."""
        folder_path: Path = settings.NANGO_TS_TYPES_FOLDER
        shutil.rmtree(folder_path)
        folder_path.mkdir()
