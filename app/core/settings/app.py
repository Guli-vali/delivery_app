"""
App level settings
"""
from typing import Any, Dict, List

from pydantic import PostgresDsn, SecretStr

from app.core.settings.base import BaseAppSettings


class AppSettings(BaseAppSettings):
    'App related settings, main class to setting up the main settings.'
    debug: bool = False
    docs_url: str = "/docs"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    title: str = "FastAPI example application"
    version: str = "0.0.0"

    database_url: PostgresDsn

    secret_key: SecretStr

    api_prefix: str = "/api"

    allowed_hosts: List[str] = ["*"]

    class Config:
        'Config related settings'
        validate_assignment = True

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        'Prepare kwargs/settings related to app itself'
        return {
            "debug": self.debug,
            "docs_url": self.docs_url,
            "openapi_prefix": self.openapi_prefix,
            "openapi_url": self.openapi_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
            "version": self.version,
        }
