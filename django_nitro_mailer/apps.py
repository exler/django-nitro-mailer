from typing import Self

from django.apps import AppConfig
from django.conf import settings


class DjangoNitroMailerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_nitro_mailer"
    verbose_name = "Django Nitro Mailer"

    def ready(self: Self) -> None:
        if getattr(settings, "NITRO_MAILER_SYNC", False):
            from django_nitro_mailer import sync_receivers  # noqa: F401
