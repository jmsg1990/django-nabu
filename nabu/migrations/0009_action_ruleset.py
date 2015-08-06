# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nabu', '0008_remove_ruleset_actions'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='ruleset',
            field=models.ForeignKey(related_name='actions', default=1, to='nabu.Ruleset'),
            preserve_default=False,
        ),
    ]
