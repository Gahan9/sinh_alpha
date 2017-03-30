from __future__ import print_function

import string

import twisted
from twisted.cred import checkers, credentials, error
from twisted.internet import defer
from zope.interface import implements
from sinh.core import credentials
from sinh.core.config import config

from zope.interface import implementer

from twisted.cred.credentials import IUsernamePassword, ICredentials

class UserDB(object):

    def __init__(self):
        self.userdb = []
        self.load()

    def load(self):
        """ load the user db file which is custom credentials
            created and stored in data/userdb.txt """

        userdb_file = '%s/userdb.txt' % (config().get('honeypot', 'data_path'),)

        f = open(userdb_file, 'r')
        while True:
            line = f.readline()
            if not line:
                break
            line = string.strip(line)
            if not line:
                continue
            (login, uid_str, passwd) = line.split(':', 2)
            uid = 0
            try:
                uid = int(uid_str)
            except ValueError:
                uid = 1001

            self.userdb.append((login, uid, passwd))

        f.close()

    def save(self):
        """ save the user db """

        userdb_file = '%s/userdb.txt' % \
            (config().get('honeypot', 'data_path'),)

        f = open(userdb_file, 'w')
        for (login, uid, passwd) in self.userdb:
            f.write('%s:%d:%s\n' % (login, uid, passwd))
        f.close()

    def checklogin(self, thelogin, thepasswd):
        """ check entered username/password against database
            note : it allows multiple passwords for a single username """

        for (login, uid, passwd) in self.userdb:
            if login == thelogin and passwd in (thepasswd, '*'):
                return True
        return False

    def user_exists(self, thelogin):
        for (login, uid, passwd) in self.userdb:
            if login == thelogin:
                return True
        return False

    def user_password_exists(self, thelogin, thepasswd):
        for (login, uid, passwd) in self.userdb:
            if login == thelogin and passwd == thepasswd:
                return True
        return False

    def getUID(self, loginname):
        for (login, uid, passwd) in self.userdb:
            if loginname == login:
                return uid
        return 1001

    def allocUID(self):
        """ allocate the next UID """

        min_uid = 0
        for (login, uid, passwd) in self.userdb:
            if uid > min_uid:
                min_uid = uid
        return min_uid + 1

    def adduser(self, login, uid, passwd):
        if self.user_password_exists(login, passwd):
            return
        self.userdb.append((login, uid, passwd))
        self.save()


class HoneypotPasswordChecker:
    """ Implemented to check SSH credentials and throw
        any error if occur regarding authentication """
    implements(checkers.ICredentialsChecker)
    credentialInterfaces = (credentials.IUsernamePassword, credentials.IPluggableAuthenticationModulesIP)

    def requestAvatarId(self, credentials):
        if hasattr(credentials, 'password'):
            if self.checkUserPass(credentials.username, credentials.password):
                return defer.succeed(credentials.username)
            else:
                return defer.fail(error.UnauthorizedLogin())
        elif hasattr(credentials, 'pamConversion'):
            return self.checkPamUser(credentials.username,
                credentials.pamConversion)
        return defer.fail(error.UnhandledCredentials())

    def checkPamUser(self, username, pamConversion):
        r = pamConversion((('Password:', 1),))
        return r.addCallback(self.cbCheckPamUser, username)

    def cbCheckPamUser(self, responses, username):
        for response, zero in responses:
            if self.checkUserPass(username, response):
                return defer.succeed(username)
        return defer.fail(error.UnauthorizedLogin())

    def checkUserPass(self, username, password):
        """ Throw attack attempt status in log by checking credentials """
        if UserDB().checklogin(username, password):
            print('login attempt [%s/%s] succeeded' % (username, password))
            return True
        else:
            print('login attempt [%s/%s] failed' % (username, password))
            return False
