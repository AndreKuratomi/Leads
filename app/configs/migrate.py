from flask import Flask
from flask_migrate import Migrate


def init_app(app: Flask):

    from app.models.app_models import Lead

    Migrate(app, app.db)
