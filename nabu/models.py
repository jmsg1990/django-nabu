# -*- coding:utf-8 -*-
import json
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from . import operators
from . import providers

# Create your models here.

class Ruleset(models.Model):

    name = models.CharField(max_length=140)

    when_creating = models.BooleanField(default=True)

    content_type = models.ForeignKey(ContentType, blank=True, null=True)

    actions = models.ManyToManyField('nabu.Action')

    def evaluate(self, instance):
        result = True

        for rule in self.rules.all():
            result = result and rule.evaluate(instance)

        return result

    def run_actions(self, ctx):
        for action in self.actions.all():
            action.execute(ctx);

    @classmethod
    def evaluate_all(cls, model, instance, created):
        for ruleset in cls.objects.all():

            result = True;

            if ruleset.content_type:
                result = result and ruleset.content_type.model_class() == model

            if result and ruleset.when_creating:
                result = result and created

            if result:
                result = ruleset.evaluate(instance)

            if result:
                ruleset.run_actions(instance)

    def __unicode__(self):
        return self.name

class Rule(models.Model):
    field = models.CharField(max_length=140)
    ruleset = models.ForeignKey('nabu.Ruleset', related_name='rules')
    operator = models.CharField(max_length=2, choices=operators.get_operators_choices())
    value = models.CharField(max_length=140)
    
    def evaluate(self, instance):
        fields = self.field.split('.');
        value = instance

        for field in fields:
            if isinstance(value, basestring):
                try:
                    value = json.loads(value)
                except:
                    value = {}

            if isinstance(value, dict):
                value = value.get(field, '')
            else:
                value = getattr(value, field, '')

            if callable(value):
                value = value()

        return self.test_rule(value, self.value)

    def test_rule(self, value1, value2):
        operator = operators.get_operator_instance(self.operator)
        if (operator):
            return operator.evaluate(value1, value2)
        return False

    def __unicode__(self):
        return u'%s %s %s' % (self.field, self.get_operator_display(), self.value)


class Action(models.Model):

    provider = models.CharField(max_length=20, choices=providers.get_providers_choices())
    name = models.CharField(max_length=140)
    data = models.TextField()

    def get_data(self):
        return json.loads(self.data)

    def get_provider(self, ctx):
        return providers.get_providers_instance(self.provider, self.get_data(), ctx)

    def execute(self, ctx):
        return self.get_provider(ctx).execute()

    def __unicode__(self):
        return self.name


#class AddressBook(models.Model):
#    contacts = models.ManyToManyField('nabu.Contact', related_name="address_books");
#
#class Contact(models.Model):
#    name = models.CharField(max_length=140)
#    email = models.EmailField()
