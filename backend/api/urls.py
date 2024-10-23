"""Load dynamically all views of the API folder into the main url router."""

import re
from importlib import import_module
from pathlib import Path
from typing import TYPE_CHECKING

from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import GenericViewSet

if TYPE_CHECKING:
    from types import ModuleType


class ConflictingUrlNamesError(Exception):
    """When several viewset have the same automatic url."""


def build_main_router() -> tuple[DefaultRouter, list[str]]:
    """Create a main router object and register the appropriate viewsets to it based on the modules and classes found in the `api` directory.

    Returns:
        DefaultRouter: The main router object with registered URL patterns.
    """
    main_router = DefaultRouter()
    url_name_list: list[str] = []

    api_dir = Path(__file__).parent
    api_modules_folders_names = [folder.name for folder in api_dir.iterdir() if folder.is_dir() and not folder.name.startswith("_")]
    for module_name in api_modules_folders_names:
        try:
            module: ModuleType = import_module(f"api.{module_name}")
        except (ImportError, ModuleNotFoundError) as error:
            print(f"Nango api's dynamic routing - Error in 'api.{module_name}'\n\t└─ {error}")  # noqa: T201
            continue
        for obj in vars(module).values():
            if isinstance(obj, type) and issubclass(obj, GenericViewSet) and obj != GenericViewSet:
                # from CamelCase to snake_case & remove "_view" (ex: MyWalletView -> my_wallet)
                url_name = re.sub(r"(?<!^)(?=[A-Z])", "_", obj.__name__).lower().replace("_view", "")
                if url_name in url_name_list:
                    error_msg: str = f"Url name {url_name} already exists"
                    raise ConflictingUrlNamesError(error_msg)
                main_router.register(url_name, obj, basename=url_name)
                url_name_list.append(url_name)

    return main_router, url_name_list


main_api_router, urls_list = build_main_router()


def get_available_routes(router: DefaultRouter = main_api_router) -> dict:
    """Return a dict with all information about available routes.

    Example:
    -------
    Example of result for the user view (with 'my_action' as additional action).
    ```
    {
        "api.user.user_views": {
            "api/user/": [
                "list",
                "create",
            ],
            "api/user/<id>/": [
                "retrieve",
                "update",
                "partial_update",
                "destroy",
            ],
            "api/user/my_action/": [
                "post",
            ],
        }
    }
    ```
    """
    classic_api_methods: list[str] = [
        "list",
        "create",
        "retrieve",
        "update",
        "partial_update",
        "destroy",
    ]
    # Regex to retrieve name from module (ex: api.user.my_user_views -> my_user)
    get_name_regex: str = r"(?<=\.)([^\.]*)_views?$"
    results: dict = {}

    for elt in router.registry:
        view = elt[1].__dict__

        view_result = {}
        base_url = f"api/{re.search(get_name_regex, view.get('__module__')).groups()[0]}"
        for attr, value in dict(view).items():
            if attr in classic_api_methods:
                url = f"{base_url}/" if attr in {"list", "create"} else f"{base_url}/<id>/"
                data = view_result.get(url, [])
                data.append(attr)
                view_result[url] = data
                continue

            value_dict = getattr(value, "__dict__", {})
            if "url_path" in value_dict:
                url = f"{base_url}/{value_dict.get('url_path')}/<id>/" if value_dict.get("detail") else f"{base_url}/{value_dict.get('url_path')}/"
                for method in value_dict.get("mapping"):
                    data = view_result.get(url, [])
                    data.append(method)
                    view_result[url] = data
        results[view.get("__module__")] = view_result
    return results
