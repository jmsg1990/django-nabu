from .base import BaseEmailBackend

from django.core.mail import EmailMessage

class DjangoEmailBackend(BaseEmailBackend):

    def __init__(self, **kwargs):
        super(DjangoEmailBackend, self).__init__(**kwargs)

        self.backend = EmailMessage(
                subject=self.subject,
                body=self.body,
                from_email=self.sender,
                to=self.recipients,
                **self.data
            )

    def send(self, **kwargs):
        self.backend.send(**kwargs)
