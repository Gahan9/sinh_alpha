import ConfigParser, os

def config():
    cfg = ConfigParser.ConfigParser()
    for f in ('sinh.cfg', '/home/jarvis/honeypot/sinh/sinh.cfg', 'honeypot/sinh/sinh.cfg'):
        if os.path.exists(f):
            cfg.read(f)
            return cfg
    return None

# vim: set sw=4 et:
