# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nabu', '0006_auto_20150806_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='rule',
            name='ruleset',
            field=models.ForeignKey(related_name='rules', default=1, to='nabu.Ruleset'),
            preserve_default=False,
        ),
    ]
