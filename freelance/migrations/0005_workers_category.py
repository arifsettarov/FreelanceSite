# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-12 16:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0004_remove_orders_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='workers',
            name='category',
            field=models.ManyToManyField(to='freelance.Work'),
        ),
    ]
