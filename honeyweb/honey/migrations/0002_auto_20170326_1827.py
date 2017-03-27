# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('honey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auth',
            name='ip',
            field=models.ForeignKey(blank=True, to='honey.Sessions', null=True),
        ),
        migrations.AlterField(
            model_name='sessions',
            name='ip',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
