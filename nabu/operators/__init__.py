# -*- coding:utf-8 -*-
NABU_OPERATORS = {}

def get_operators_choices():
    return tuple(map(lambda x: (x.getName(), x.getDescription()), NABU_OPERATORS.values()))

def get_operator_instance(name):
    provider = NABU_OPERATORS.get(name, None)
    if provider:
        return provider()

from .eq import EQOperator
EQOperator.register(NABU_OPERATORS)
