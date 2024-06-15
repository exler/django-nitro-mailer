from typing import Any

from django.db.models.signals import post_save
from django.dispatch import receiver

from django_nitro_mailer.models import Email


@receiver(post_save, sender=Email)
def send_email(sender: type[Email], instance: Email, **kwargs: Any) -> None:
    # TODO: Immediately send the email and log the result.
    pass
