# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-13 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0009_auto_20170512_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_DATA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('password', models.CharField(max_length=100, verbose_name='Пароль')),
                ('user_id', models.IntegerField()),
            ],
        ),
    ]
