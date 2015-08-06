# -*- coding:utf-8 -*-

class RegistryMixin:
    @classmethod
    def getName(cls):
        return cls.name

    @classmethod
    def getDescription(cls):
        return cls.description

    @classmethod
    def register(cls, registry):
        registry[cls.getName()] = cls

