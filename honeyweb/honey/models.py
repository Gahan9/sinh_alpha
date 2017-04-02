from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import django_tables2 as tables
from django.db import models


@python_2_unicode_compatible
class Sessions(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField(blank=True, null=True)
    sensor = models.IntegerField()
    ip = models.CharField(max_length=15, null=True)
    termsize = models.CharField(max_length=7, blank=True, null=True)
    client = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.ip

    class Meta:
        db_table = 'sessions'


class Auth(models.Model):
    session = models.CharField(max_length=32)
    success = models.BooleanField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    timestamp = models.DateTimeField()

    @property
    def get_ip_from_session(self):
        obj_session = Sessions.objects.filter(id=Auth.objects.all()[0].session)
        return obj_session[0].ip

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'auth'


class Clients(models.Model):
    version = models.CharField(max_length=50)

    def __unicode__(self):
        return self.version

    class Meta:
        db_table = 'clients'


class Downloads(models.Model):
    session = models.CharField(max_length=32)
    timestamp = models.DateTimeField()
    url = models.TextField()
    outfile = models.TextField()

    class Meta:
        db_table = 'downloads'


class Input(models.Model):
    session = models.CharField(max_length=32)
    timestamp = models.DateTimeField()
    realm = models.CharField(max_length=50, blank=True, null=True)
    success = models.IntegerField(blank=True, null=True)
    input = models.TextField()

    class Meta:
        db_table = 'input'


class InputTable(tables.Table):
    class Meta:
        model = Input
        exclude = ['realm']
        attrs = {'class': 'table table-hover'}


class Sensors(models.Model):
    ip = models.CharField(max_length=15)

    class Meta:
        db_table = 'sensors'


class Ttylog(models.Model):
    session = models.CharField(max_length=32)
    ttylog = models.TextField()

    class Meta:
        db_table = 'ttylog'
