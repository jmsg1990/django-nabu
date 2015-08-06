# -*- coding:utf-8 -*-

from .base import BaseEmailBackend

import smtplib
from email.mime.text import MIMEText

class SimpleEmailBackend(BaseEmailBackend):

    def __init__(self, **kwargs):
        super(SimpleEmailBackend, self).__init__(**kwargs)

        self.smtp_options = kwargs.get('smtp_options', {
                "host": "localhost",
                "port": None,
                "use_ssl": False,
                "user": None,
                "password": ''
            })

    def build_message(self):
        msg = MIMEText(self.body)
        msg['Subject'] = self.subject
        msg['From'] = self.sender
        msg['To'] = ','.join(self.recipients)
        
        return msg

    def get_smtp_provider(self):
        if self.smtp_options['use_ssl']:
            return smtplib.SMTP_SSL
        return smtplib.SMTP

    def send(self):

        SMTP = self.get_smtp_provider()
        s = SMTP(str(self.smtp_options['host']), str(self.smtp_options['port']))

        if self.smtp_options['user']:
            s.login(str(self.smtp_options['user']), str(self.smtp_options['password']))

        s.sendmail(self.sender, self.recipients, self.build_message().as_string())
        s.quit()
