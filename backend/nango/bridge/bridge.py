"""Class for Nango's bridge.

Structure of model's settings:
-----------------------------
{
    'serializers': {
        'simple': {
            'fields': [],
            'write_only_fields': [],
            'read_only_fields': [],
        },
        'detail': {
            'fields': [],
            'write_only_fields': [],
            'read_only_fields': [],
        },
        'global_fields': {
            'fields': [],
            'write_only_fields': [],
            'read_only_fields': [],
        },
    },
    'view': {
        queryset: "all" | "user_centric" (default=all)
    },
}

Model's settings that Nango handle:
----------------
None: Nothing will be created.

{'serializers': None }: No serializer will be created.
{'serializers': {'simple' | 'detail': None} }: No simple (resp. detail) serializer will be created.
{'view': None} : The view of the model wil not be created.

"""

import re
import shutil
from datetime import datetime
from pathlib import Path
from pprint import pprint

from django.apps import apps
from django.conf import settings
from django.db.models import fields
from django.db.models.base import ModelBase
from django.db.models.fields.related import Field, ManyToManyField, RelatedField
from django.db.models.fields.reverse_related import ManyToOneRel
from jinja2 import Environment, FileSystemLoader


def from_camelcase_to_snakecase(string_to_convert: str) -> str:
    """Convert CamelCase string to snake_case."""
    words = re.findall(r"\b[A-Z][a-z]*\b|[A-Z]?[a-z]+|[A-Z]{2,}(?=[A-Z][a-z]|\d|\W|$)|\d+", string_to_convert)
    return "_".join(word.lower() for word in words)


class FileManager:
    """Create API files: Views & Serializers.

    Structure of models_data:
    {
        Model_object: {
            field1_objects: typefield1,
            field2_objects: typefield2,
            ...
        },
        ...
    }
    All `typefield` are python types corresponding to django's `field_object`.
    """

    def __init__(self, model_list: list[ModelBase] = ()) -> None:
        self.model_list: list[ModelBase] = model_list

        self.api_folder_path: Path = settings.ROOT_DIR / "api"
        self.nango_cache_folder_path = self.make_cache_folder()
        self._template_path: Path = settings.ROOT_DIR / "nango/templates"
        self.jinja_env = Environment(
            loader=FileSystemLoader(self._template_path),
            autoescape=True,
        )
        self.default_settings: dict[str, any] = {
            "serializers": {
                "simple": {},
                "detail": {},
            },
            "view": {},
        }

    def make_cache_folder(self) -> Path:
        """Create the cache folder if it doesn't exists.

        Return cache_folderpath
        """
        cache_folder_path = self.api_folder_path / "_nango_cache"
        if cache_folder_path.exists():
            return cache_folder_path
        cache_folder_path.mkdir(parents=False, exist_ok=True)

        # __init__.py & .gitignore
        cache_init_file_path = cache_folder_path / "__init__.py"
        cache_init_file_path.touch(exist_ok=True)
        cache_gitignore_file_path = cache_folder_path / ".gitignore"
        cache_gitignore_file = cache_gitignore_file_path.open("a")
        cache_gitignore_file.write("*")
        cache_gitignore_file.close()

        return cache_folder_path

    def make_api_architecture(self, model_name: str) -> None:
        """Create the API architecture with the given name.

        It setup main folder, views folder, serializers folder and __init__.py files.
        In API folder & in _nango_cache folder
        """
        snake_case_model_name: str = from_camelcase_to_snakecase(model_name)
        if not isinstance(model_name, str):
            raise TypeError

        def _make_architecture(folder_path: Path) -> None:
            if not folder_path.exists():
                folder_path.mkdir()

            if "_nango_cache" in str(folder_path):
                suffix: str = "nango_"
            else:
                suffix = ""

            init = folder_path.joinpath("__init__.py")
            init.touch()
            init_file = init.open("w")
            init_file.write(f"from .{snake_case_model_name}_detail_{suffix}serializer import *\n")
            init_file.write(f"from .{snake_case_model_name}_{suffix}serializer import *\n")
            if suffix != "nango_":
                init_file.write(f"from .{snake_case_model_name}_{suffix}views import *\n")
            init_file.close()

        _make_architecture(self.nango_cache_folder_path / snake_case_model_name)
        _make_architecture(self.api_folder_path / snake_case_model_name)

    def _render_template(self, template_name: str, data: dict, target_file_path: Path) -> None:
        """Populate the `template_name` (.j2 file) with `data` and render it to the `target_file_path` location."""
        if not isinstance(data, dict):
            raise TypeError
        if not template_name.endswith(".j2"):
            error_msg: str = "The template must be a .j2 file."
            raise ValueError(error_msg)
        if not self._template_path.joinpath(template_name).exists():
            error_msg: str = f"{self._template_path.joinpath(template_name)} does not exists."

        # Render template
        template = self.jinja_env.get_template(template_name)
        content = template.render(**data)

        # Write content to file
        target_file = target_file_path.open("w")
        target_file.write(content)
        target_file.close()

    def _make_serializer(self, folder_path: Path, data: dict, *, detail: bool) -> None:
        model_name: str = folder_path.name

        if "_nango_cache" in str(folder_path):
            suffix = "detail_nango_serializer" if detail else "nango_serializer"
            serializer_file_path: Path = folder_path / f"{from_camelcase_to_snakecase(model_name)}_{suffix}.py"
            self._render_template(template_name=f"{suffix}.j2", data=data, target_file_path=serializer_file_path)
        else:
            suffix = "detail_serializer" if detail else "serializer"
            serializer_file_path: Path = folder_path / f"{from_camelcase_to_snakecase(model_name)}_{suffix}.py"
            if serializer_file_path.exists():
                # Do NOT overwrite user's file
                return
            self._render_template(template_name="basic_serializer.j2", data=data, target_file_path=serializer_file_path)

    def make_serializer_file(
        self,
        model: ModelBase,
        model_data: dict[fields, str],  # type: ignore  # noqa: PGH003
        *,
        detail: bool,
    ) -> None:
        """Create a serializer file for a given model_data.

        End directly if the serializer file already exists.
        Detail argument specify if the serializer is a detail one or not.
        """
        model_name = model.__name__
        snake_case_model_name: str = from_camelcase_to_snakecase(model.__name__)

        # Build customizable user's serializer
        nango_serializer_name: str = f"{model_name}{'Detail' if detail else ''}NangoSerializer"
        regex = r"(?<=')(.*)(?=\.)"
        match = re.search(regex, str(model))
        import_path = match.group(1)
        data = {
            "imports": [
                f"from api._nango_cache.{snake_case_model_name}.{snake_case_model_name}{"_detail" if detail else ""}"
                f"_nango_serializer import {nango_serializer_name}",
                f"from {import_path} import {model_name}",
            ],
            "model_name": model_name,
            "serializer_name": f"{model_name}{'Detail' if detail else ''}Serializer",
            "nango_serializer": nango_serializer_name,
        }
        self._make_serializer(folder_path=self.api_folder_path / snake_case_model_name, data=data, detail=detail)

        # Build generated Nango's serializer
        data = {
            "imports": [
                f"from {import_path} import {model_name}",
            ],
            "model_name": model_name,
        }
        if detail:
            data["detail"] = {
                "field_names_list": [field.name for field in model_data],
                "specified_fields": [
                    {
                        "name": key.related_name if isinstance(key, ManyToOneRel) else key.name,
                        "model_name": key.related_model.__name__,
                        "serializer": f"{key.related_model.__name__}Serializer",
                        "many": isinstance(key, ManyToOneRel | ManyToManyField),
                    }
                    for key, value in model_data.items()
                    if value
                    in [
                        "ForeignKey",
                        "ManyToManyField",
                        "OneToOneField",
                    ]
                    and key.related_model in self.model_list
                ],
            }
            data["imports"] = [
                f"from api.{from_camelcase_to_snakecase(dico.get('model_name'))}.{from_camelcase_to_snakecase(dico.get('model_name'))}"
                f"_serializer import {dico.get('serializer')}"
                for dico in data["detail"]["specified_fields"]
            ] + data["imports"]
        else:
            data["simple"] = {
                "field_names_list": [field.name for field in model_data],
            }
        self._make_serializer(folder_path=self.nango_cache_folder_path / snake_case_model_name, data=data, detail=detail)

    def edit_serializer_fields(self) -> None:
        r"""Edit fields to match with the model config if exists.

        re -> fields:.*=\s*\[(?:[^\]\[]|\[(?:[^\]\[]|\[(?R)\])*\])*\],
        """

    def make_view(self, model: ModelBase, model_data: dict[fields, str]) -> None:  # noqa: ARG002
        """Create a view file for a given model_data."""
        snake_case_model_name: str = from_camelcase_to_snakecase(model.__name__)
        view_path: Path = self.api_folder_path / snake_case_model_name / f"{snake_case_model_name}_views.py"
        if view_path.exists():
            return

        # Build data
        regex = r"(?<=')(.*)(?=\.)"
        match = re.search(regex, str(model))
        import_path = match.group(1)
        data = {
            "imports": [
                f"from {import_path} import {model.__name__}",
            ],
            "model_name": model.__name__,
            "model_name_snake_case": snake_case_model_name,
        }

        # Render template
        view_template = self.jinja_env.get_template("view.j2")
        content = view_template.render(**data)

        # Write content to file
        view_file = view_path.open("w")
        view_file.write(content)
        view_file.close()

    def get_model_settings(self, model: ModelBase) -> dict[str, any] | None:
        """Get settings of a given model."""
        try:
            return model.nango()
        except AttributeError:
            return self.default_settings

    def setup_api_for_model(self, models_data: dict[ModelBase, dict[fields, str]]) -> None:
        """Setup API files for a given model."""
        for model in models_data:
            model_name = model.__name__

            # Check settings for folder construction
            settings = self.get_model_settings(model)
            if settings is None or settings["serializers"] is None and settings["view"] is None:
                continue

            self.make_api_architecture(model_name=model_name)
            if settings["serializers"]["simple"] is not None:
                self.make_serializer_file(model=model, model_data=models_data[model], detail=False)
            if settings["serializers"]["detail"] is not None:
                self.make_serializer_file(model=model, model_data=models_data[model], detail=True)
            if settings["view"] is not None:
                self.make_view(model=model, model_data=models_data[model])


class Bridge:
    """Transform models into API views.

    A `typefield` is the python type for a given model field.
    If you want to handle from Django's type fields, please custom the `Bridge._get_typefield_from_field`'s match case method.
    """

    def __init__(self, **kwargs: dict[str, any]) -> None:
        self.models_typefields: dict[str, dict[str, str]] = {}
        self._force = kwargs.get("force", False)
        self.model_list: list[ModelBase] = []
        self._forbidden_fields: list[str] = [
            "password",
            "outstandingtoken",
        ]

    def get_models(self) -> list[ModelBase]:
        """Return all models in the project.

        Do not contain third party libraries and model with 'None' as Nango parameters.
        """

        def _default_dict_method() -> dict:
            return {}

        self.model_list = []

        for model in apps.get_models():
            library_model = model.__module__.startswith("django") or model.__module__.startswith("rest_framework")
            nango_method = getattr(model, "nango", _default_dict_method)
            if not library_model and nango_method() is not None:
                self.model_list.append(model)

        return self.model_list

    def _get_fields_from_models(self, models: list[ModelBase]) -> dict[ModelBase, list[fields]]:
        """Return all fields of each model of the `models` list."""
        result = {}
        for model in models:
            fields_list: list[Field] = []

            for field in model._meta.get_fields():  # noqa: SLF001
                if not isinstance(field, RelatedField | ManyToOneRel):
                    fields_list.append(field)
                    continue

                if field.related_model in self.model_list:
                    fields_list.append(field)

            result[model] = fields_list
        return result

    def _get_typefield_from_field(self, field: fields) -> str:
        """Return the python type of a field."""
        model_field_type_str = field.get_internal_type()
        match model_field_type_str:
            case "CharField" | "TextField":
                return str
            case "IntegerField" | "PositiveIntegerField" | "SmallIntegerField" | "BigAutoField" | "BigIntegerField":
                return int
            case "FloatField":
                return float
            case "BooleanField":
                return bool
            case "DateTimeField" | "DateField" | "TimeField":
                return datetime
            case _:
                return model_field_type_str

    def get_typefields_from_models(self) -> dict[ModelBase, {fields, str}]:
        """From each model, return field_name with its python type."""
        models: list[ModelBase] = self.get_models()
        models_fields: dict[ModelBase, list[fields]] = self._get_fields_from_models(models)

        models_typefields: dict[ModelBase, {fields, str}] = {}
        for model, model_fields in models_fields.items():
            models_typefields[model] = {}
            for field in model_fields:
                if field.name in self._forbidden_fields:
                    continue
                models_typefields[model][field] = self._get_typefield_from_field(field=field)

        self.models_typefields = models_typefields
        return models_typefields

    def run(self) -> None:
        """Execute the bridge."""
        models_typefields = self.get_typefields_from_models()
        file_manager = FileManager(model_list=self.model_list)
        file_manager.setup_api_for_model(models_data=models_typefields)

    def clean(self) -> None:
        """Clean the nango_cache folder."""
        file_manager = FileManager()
        shutil.rmtree(settings.ROOT_DIR / "api" / "_nango_cache")
        file_manager.make_cache_folder()


if __name__ == "__main__":
    from utils import setup_django

    setup_django()

    b = Bridge()
    b.run()
    from api.author import AuthorDetailSerializer, AuthorSerializer

    from nango.models import Author

    serializer = AuthorSerializer(Author.objects.all(), many=True)
    pprint(list(serializer.data))  # noqa: T203
    serializer = AuthorDetailSerializer(Author.objects.all(), many=True)
    pprint(list(serializer.data))  # noqa: T203

    from api.urls import main_api_router

    print(main_api_router.urls)  # noqa: T201
