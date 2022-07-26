"""
Test environment specific settings
"""
from pydantic import PostgresDsn, SecretStr

from app.core.settings.app import AppSettings


class TestAppSettings(AppSettings):
    'Seevice app settings'
    debug: bool = True

    title: str = "Test FastAPI example application"

    secret_key: SecretStr = SecretStr("test_secret")

    database_url: PostgresDsn
