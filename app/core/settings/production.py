"""
Production environment specific settings
"""
from app.core.settings.app import AppSettings


class ProdAppSettings(AppSettings):
    'Seevice app settings'
    class Config(AppSettings.Config):
        'Config related settings'
        env_file = "prod.env"
