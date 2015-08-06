# -*- coding:utf-8 -*-

NABU_PROVIDERS = {}

def get_providers_choices():
    return tuple(map(lambda x: (x.getName(), x.getDescription()), NABU_PROVIDERS.values()))

def get_providers_instance(name, data, ctx):
    provider = NABU_PROVIDERS.get(name, None)
    if provider:
        return provider(data, ctx)

from .email import EmailProvider
EmailProvider.register(NABU_PROVIDERS)
