from __future__ import print_function
import ConfigParser, os

def config():
    """Parsing the Config file stored in root directory"""
    cfg = ConfigParser.ConfigParser()
    # get_path = lambda x: os.path.abspath(os.path.join(os.path.dirname(__file__), x))
    # DATA_DIR = get_path('sinh.cfg')
    # for files in os.listdir(DATA_DIR):
    #     f_p = open(os.path.join(DATA_DIR, files))

    # for f in f_p:
    for f in ('sinh.cfg', 'sinh/sinh.cfg'):
        if os.path.exists(f):
            cfg.read(f)
            return cfg
    return None

