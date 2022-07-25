"""
Reference utils for settings instalation
"""
from enum import Enum

from pydantic import BaseSettings


class AppEnvTypes(Enum):
    'Application environments types for settings'
    PROD: str = "prod"
    DEV: str = "dev"
    TEST: str = "test"


class BaseAppSettings(BaseSettings):
    'Abstract settings class'
    app_env: AppEnvTypes = AppEnvTypes.PROD

    class Config:
        'Config related settings'
        env_file = ".env"
