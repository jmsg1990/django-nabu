# -*- coding:utf-8 -*-

from .base import BaseProvider
from ..backends.email.django_backend import DjangoEmailBackend

from django.template import Context, Template

class EmailProvider(BaseProvider):

    name = 'email'
    description = 'Email Provider'

    def __init__(self, data=None, ctx={}):
        super(EmailProvider, self).__init__(data)

        self.recipients = self.data.pop('recipients', []);
        self.sender = self.data.pop('sender', '');
        self.subject = self.data.pop('subject', '');
        self.body = self.data.pop('body', '');

        self.context = ctx

        self.backend = self.data.pop('backend', DjangoEmailBackend)
    
    def get_recipients(self):
        if hasattr(self, 'action_counter'):
            return self.recipients[self.action_counter % len(self.recipients)]
        return self.recipients[0]

    def get_sender(self):
        return self.sender

    def get_email_body(self):
        template = Template(self.body)
        context = Context({"ctx": self.context })
        return template.render(context)

    def get_subject(self):
        return self.subject

    def get_email_backend(self):
        return self.backend

    def init_backend(self):
        Backend = self.get_email_backend()
        self.backend_instance = Backend(
                sender = self.get_sender(),
                subject = self.get_subject(),
                recipients = self.get_recipients(),
                body = self.get_email_body(),
                **self.data
            )
        
        return self.backend_instance

    def send_email(self):
        self.init_backend();
        self.backend_instance.send();

    def execute(self, nabuAction, **kwargs):
        self.action_counter = nabuAction.counter
        
        nabuAction.counter += 1
        nabuAction.save();

        return self.send_email(**kwargs)
