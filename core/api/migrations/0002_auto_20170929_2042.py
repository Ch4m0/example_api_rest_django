# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 20:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='propietario',
        ),
        migrations.DeleteModel(
            name='ToDo',
        ),
    ]