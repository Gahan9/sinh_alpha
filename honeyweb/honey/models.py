from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import django_tables2 as tables
from django.db import models


class Sessions(models.Model):
    """ MySql table which stores session start and end """
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
        db_table = 'sessions'  # override table name honey.sessions to sessions in MySql Database


class SessionsTable(tables.Table):
    """ Created Table to show in template tag """
    starttime = tables.Column('Session Started at')
    endtime = tables.Column('Session Ended at')
    sensor = tables.Column('Sensor ID')
    ip = tables.Column('IP Address')
    client = tables.Column('Client ID')

    class Meta:
        model = Sessions
        exclude = ['termsize']
        attrs = {'class': 'table table-hover'}  # adds attribute class to load bootstrap3 CSS


class Auth(models.Model):
    """ MySql table which stores credentials through which attacker got access """
    session = models.CharField(max_length=32)
    success = models.BooleanField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    timestamp = models.DateTimeField()

    # property defined to retrive Ip address of attacker stored in sessions' table
    @property
    def get_ip_from_session(self):
        obj_session = Sessions.objects.filter(id=Auth.objects.all()[0].session)
        return obj_session[0].ip

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'auth'  # override table name honey.auth to auth in MySql Database


class AuthTable(tables.Table):
    """ Created Table to show in template tag """
    # get_ip_from_session = tables.Column('IP address')
    success = tables.BooleanColumn('Status', yesno='Access Granted, Access Denied')
    timestamp = tables.Column('Timestamp')

    class Meta:
        model = Auth
        attrs = {'class': 'table table-hover'}  # adds attribute class to load bootstrap3 CSS


class Clients(models.Model):
    """ MySql table - stores attacker's SSH client version """
    version = models.CharField(max_length=50)

    def __unicode__(self):
        return self.version

    class Meta:
        db_table = 'clients'   # override table name honey.clients to clients in MySql Database


class ClientsTable(tables.Table):
    """ Created Table to show in template tag """
    class Meta:
        model = Clients
        attrs = {'class': 'table table-hover'}  # adds attribute class to load bootstrap3 CSS


class Downloads(models.Model):
    session = models.CharField(max_length=32)
    timestamp = models.DateTimeField()
    url = models.TextField()
    outfile = models.TextField()

    class Meta:
        db_table = 'downloads'   # override table name


class DownloadsTable(tables.Table):
    """ Created Table to show in template tag """
    url = tables.Column('URL')
    timestamp = tables.Column('Timestamp')
    outfile = tables.Column('File path')

    class Meta:
        model = Downloads
        attrs = {'class': 'table table-hover'}  # adds attribute class to load bootstrap3 CSS


class Input(models.Model):
    """ MySql table stores every executed/non-executed commands from attacker """
    session = models.CharField(max_length=32)
    timestamp = models.DateTimeField()
    realm = models.CharField(max_length=50, blank=True, null=True)
    success = models.IntegerField(blank=True, null=True)
    input = models.TextField()

    class Meta:
        db_table = 'input'   # override table name


class InputTable(tables.Table):
    """ Created Table to show in template tag """
    success = tables.BooleanColumn('Command Executed?', yesno='Yes,No')
    timestamp = tables.Column('Timestamp')

    class Meta:
        model = Input
        exclude = ['realm']
        attrs = {'class': 'table table-hover'}  # adds attribute class to load bootstrap3 CSS


class Sensors(models.Model):
    """ Honeypot sensor table (Own IP) """
    ip = models.CharField(max_length=15)

    class Meta:
        db_table = 'sensors'   # override table name


class SensorsTable(tables.Table):
    """ Created Table to show in template tag """
    ip = tables.Column("IP Address of  Honeypot  Server")

    class Meta:
        model = Sensors
        attrs = {'class': 'table table-hover'}  # adds attribute class to load bootstrap3 CSS


class Ttylog(models.Model):
    """ Binary log table """
    session = models.CharField(max_length=32)
    ttylog = models.TextField()

    class Meta:
        db_table = 'ttylog'   # override table name


class TtylogTable(tables.Table):
    """ Created Table to show in template tag """
    class Meta:
        model = Ttylog
        attrs = {'class': 'table table-hover'}  # adds attribute class to load bootstrap3 CSS

