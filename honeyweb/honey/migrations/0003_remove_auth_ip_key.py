# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 04:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('honey', '0002_auto_20170328_1813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auth',
            name='ip_key',
        ),
    ]
