# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nabu', '0002_auto_20150804_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('provider', models.CharField(max_length=20, choices=[(b'email', b'Email Provider')])),
                ('name', models.CharField(max_length=140)),
                ('data', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='addressbook',
            name='contacts',
        ),
        migrations.RemoveField(
            model_name='ruleset',
            name='from_address',
        ),
        migrations.RemoveField(
            model_name='ruleset',
            name='recipients',
        ),
        migrations.DeleteModel(
            name='AddressBook',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.AddField(
            model_name='ruleset',
            name='actions',
            field=models.ManyToManyField(to='nabu.Action'),
        ),
    ]
