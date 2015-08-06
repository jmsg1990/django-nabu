# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddressBook',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('field', models.CharField(max_length=140)),
                ('operator', models.CharField(max_length=2, choices=[('eq', 'Igual a')])),
                ('value', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Ruleset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=140)),
                ('from_address', models.EmailField(max_length=254)),
                ('recipients', models.ManyToManyField(related_name='rulesets', to='nabu.AddressBook')),
                ('rules', models.ManyToManyField(related_name='rulesets', to='nabu.Rule')),
            ],
        ),
        migrations.AddField(
            model_name='addressbook',
            name='contacts',
            field=models.ManyToManyField(related_name='address_books', to='nabu.Contact'),
        ),
    ]
