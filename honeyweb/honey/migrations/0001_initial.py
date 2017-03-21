# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('session', models.CharField(max_length=32)),
                ('success', models.BooleanField()),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth',
            },
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'clients',
            },
        ),
        migrations.CreateModel(
            name='Downloads',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('session', models.CharField(max_length=32)),
                ('timestamp', models.DateTimeField()),
                ('url', models.TextField()),
                ('outfile', models.TextField()),
            ],
            options={
                'db_table': 'downloads',
            },
        ),
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('session', models.CharField(max_length=32)),
                ('timestamp', models.DateTimeField()),
                ('realm', models.CharField(max_length=50, null=True, blank=True)),
                ('success', models.IntegerField(null=True, blank=True)),
                ('input', models.TextField()),
            ],
            options={
                'db_table': 'input',
            },
        ),
        migrations.CreateModel(
            name='Sensors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'sensors',
            },
        ),
        migrations.CreateModel(
            name='Sessions',
            fields=[
                ('id', models.CharField(max_length=32, serialize=False, primary_key=True)),
                ('starttime', models.DateTimeField()),
                ('endtime', models.DateTimeField(null=True, blank=True)),
                ('sensor', models.IntegerField()),
                ('ip', models.CharField(max_length=15)),
                ('termsize', models.CharField(max_length=7, null=True, blank=True)),
                ('client', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'sessions',
            },
        ),
        migrations.CreateModel(
            name='Ttylog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('session', models.CharField(max_length=32)),
                ('ttylog', models.TextField()),
            ],
            options={
                'db_table': 'ttylog',
            },
        ),
    ]
