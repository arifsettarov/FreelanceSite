# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-13 10:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0015_workers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workers',
            name='region',
        ),
        migrations.RemoveField(
            model_name='workers',
            name='type',
        ),
    ]