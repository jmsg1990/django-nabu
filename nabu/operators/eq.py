# -*- coding:utf-8 -*-
from .base import BaseOperator

class EQOperator(BaseOperator):
    name = 'eq'
    description = 'Igual a'

    def evaluate(self, value1, value2):
        return value1 == value2
