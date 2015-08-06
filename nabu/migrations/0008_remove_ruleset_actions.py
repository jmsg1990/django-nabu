# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nabu', '0007_rule_ruleset'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ruleset',
            name='actions',
        ),
    ]
