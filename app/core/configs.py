import os
from functools import lru_cache
from typing import Dict, Type

from app.core.settings.app import AppSettings
from app.core.settings.development import DevAppSettings
from app.core.settings.production import ProdAppSettings
from app.core.settings.test import TestAppSettings

environments: Dict[str, Type[AppSettings]] = {
    "dev": DevAppSettings,
    "prod": ProdAppSettings,
    "test": TestAppSettings,
}


@lru_cache
def get_app_settings() -> AppSettings:
    app_env = os.environ.get("environment", "dev")
    print("app_env::", app_env)
    config = environments[app_env]
    settings = config()
    return settings
