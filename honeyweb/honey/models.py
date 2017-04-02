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
        # return '%s , %s' % (self.id, self.ip)
        return self.ip

    class Meta:
        # managed = False
        db_table = 'sessions'


class Auth(models.Model):
    session = models.CharField(max_length=32)
    success = models.BooleanField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    # ip_key = models.ForeignKey(Sessions, blank=True, null=True, default='')

    @property
    def get_ip_from_session(self):
        obj_session = Sessions.objects.filter(id=Auth.objects.all()[0].session)
        return obj_session[0].ip

    def __str__(self):
        return self.username

    class Meta:
        # managed = False
        db_table = 'auth'


# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=80)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group'
#
#
# class AuthGroupPermissions(models.Model):
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)
#
#
# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)
#
#
# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user'
#
#
# class AuthUserGroups(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)
#
#
# class AuthUserUserPermissions(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)


class Clients(models.Model):
    version = models.CharField(max_length=50)

    def __unicode__(self):
        return self.version

    class Meta:
    #     # managed = False
        db_table = 'clients'


# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.SmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'
#
#
# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)
#
#
# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_migrations'
#
#
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_session'


class Downloads(models.Model):
    session = models.CharField(max_length=32)
    timestamp = models.DateTimeField()
    url = models.TextField()
    outfile = models.TextField()

    class Meta:
    #     # managed = False
        db_table = 'downloads'


# class HoneyQuestion(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField()
#
    # class Meta:
#         managed = False
#         db_table = 'honey_question'


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
