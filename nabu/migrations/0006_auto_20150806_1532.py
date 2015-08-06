# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nabu', '0005_auto_20150806_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rulerelation',
            name='rule',
        ),
        migrations.RemoveField(
            model_name='rulerelation',
            name='ruleset',
        ),
        migrations.RemoveField(
            model_name='ruleset',
            name='rules',
        ),
        migrations.DeleteModel(
            name='RuleRelation',
        ),
    ]
