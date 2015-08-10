# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nabu', '0010_auto_20150806_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='counter',
            field=models.BigIntegerField(default=0),
        ),
    ]
