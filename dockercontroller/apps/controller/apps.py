"""App definition"""

from django.apps import AppConfig


class ControllerConfig(AppConfig):
    """Controller config"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "dockercontroller.apps.controller"
