# -*- coding:utf-8 -*-

class BaseEmailBackend(object):

    def __init__(self, **kwargs):
        self.data = kwargs
        self.sender = self.data.pop('sender', '')
        self.recipients = self.data.pop('recipients', [])
        self.subject = self.data.pop('subject', '')
        self.body = self.data.pop('body', '')

    def send(self):
        pass

    def build_message(self):
        pass
