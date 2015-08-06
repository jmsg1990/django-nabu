# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nabu', '0004_remove_ruleset_rules'),
    ]

    operations = [
        migrations.CreateModel(
            name='RuleRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rule', models.ForeignKey(to='nabu.Rule')),
                ('ruleset', models.ForeignKey(to='nabu.Ruleset')),
            ],
        ),
        migrations.AddField(
            model_name='ruleset',
            name='rules',
            field=models.ManyToManyField(related_name='rulesets', through='nabu.RuleRelation', to='nabu.Rule'),
        ),
    ]
