# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='hecho',
            field=models.TextField(default=False),
        ),
    ]