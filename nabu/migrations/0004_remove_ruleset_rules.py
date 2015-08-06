# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nabu', '0003_auto_20150805_2021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ruleset',
            name='rules',
        ),
    ]
