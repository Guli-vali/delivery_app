"""
Development environment specific settings
"""
from app.core.settings.app import AppSettings


class DevAppSettings(AppSettings):
    'Seevice app settings'
    debug: bool = True
    title: str = "Dev FastAPI example application"

    class Config(AppSettings.Config):
        'Config related settings'
        env_file = ".env"
