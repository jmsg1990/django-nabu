# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nabu', '0009_action_ruleset'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='action',
            name='ruleset',
        ),
        migrations.AddField(
            model_name='ruleset',
            name='actions',
            field=models.ManyToManyField(to='nabu.Action'),
        ),
    ]
