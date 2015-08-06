# -*- coding:utf-8 -*-

from ..base import RegistryMixin

class BaseOperator(RegistryMixin):
    def evaluate(self):
        return True
