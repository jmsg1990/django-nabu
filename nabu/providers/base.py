# -*- coding:utf-8 -*-

from ..base import RegistryMixin


class BaseProvider(object, RegistryMixin):

    def __init__(self, data=None):
        self.data = data

    def get_data(self):
        return self.data

    def execute(self, nabuAction):
        """
        This method is the entry point for the providers
        """
        return
