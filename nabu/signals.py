# -*- coding:utf-8 -*-
from django.db.models.signals import post_save
from .models import Ruleset

def post_create_handler(sender, instance, created, **kwars):
    Ruleset.evaluate_all(sender, instance, created)

post_save.connect(post_create_handler, dispatch_uid="nabu_ruleset_eval")
