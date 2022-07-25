"""
Entry point of app
"""
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.routes.api import router as api_router
from app.core.settings.app import AppSettings
from app.core.config import settings as app_settings


def setup_middlewaries(application: FastAPI, settings: AppSettings) -> None:
    'Setting up middlewares'
    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_hosts,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def setup_routes(application: FastAPI, settings: AppSettings) -> None:
    'Setting up routes of app'
    @application.get(
        '/',
        name="core:healthcheck"
    )
    def healthchek():
        return {"ping": "pong"}

    application.include_router(api_router, prefix=settings.api_prefix)


def get_application(settings: AppSettings) -> FastAPI:
    'Assemble app applying all needed components'
    application = FastAPI(**settings.fastapi_kwargs)

    setup_routes(application, settings)
    setup_middlewaries(application, settings)

    return application


app = get_application(app_settings)
