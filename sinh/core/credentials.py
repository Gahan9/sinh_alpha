
from zope.interface import implementer

from twisted.cred.credentials import IUsernamePassword, \
    ICredentials


class IUsername(ICredentials):
    """
    Encapsulate username only

    @type username: C{str}
    @ivar username: The username associated with these credentials.
    """


class IUsernamePasswordIP(IUsernamePassword):
    """
    This encapsulate a username, a plaintext password and a source IP

    @type username: C{str}
    @ivar username: The username associated with these credentials.

    @type password: C{str}
    @ivar password: The password associated with these credentials.

    @type ip: C{str}
    @ivar ip: The source ip address associated with these credentials.
    """


class IPluggableAuthenticationModulesIP(ICredentials):
    """
    Twisted removed IPAM in 15, adding in Cowrie now
    """


@implementer(IPluggableAuthenticationModulesIP)
class PluggableAuthenticationModulesIP(object):
    """
    Twisted removed IPAM in 15 trying to add support for Twisted version above 15
    """

    def __init__(self, username, pamConversion, ip):
        self.username = username
        self.pamConversion = pamConversion
        self.ip = ip


@implementer(IUsername)
class Username(object):
    """
    """
    def __init__(self, username):
        self.username = username


@implementer(IUsernamePasswordIP)
class UsernamePasswordIP(object):
    """
    This credential interface also provides an IP address
    """
    def __init__(self, username, password, ip):
        self.username = username
        self.password = password
        self.ip = ip

