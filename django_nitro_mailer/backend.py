from typing import Self

from django.conf import settings
from django.core.mail import EmailMessage
from django.core.mail.backends.base import BaseEmailBackend

from django_nitro_mailer.models import Email


class DatabaseBackend(BaseEmailBackend):
    EMAIL_BATCH_SIZE = getattr(settings, "NITRO_MAILER_EMAIL_BATCH_SIZE", None)

    def send_messages(self: Self, email_messages: list[EmailMessage]) -> int:
        email_objs = []
        for email in email_messages:
            email_obj = Email()
            email_obj.set_email(email)
            email_objs.append(email_obj)

        email_objs = Email.objects.bulk_create(email_objs, batch_size=self.EMAIL_BATCH_SIZE)
        return len(email_objs)
