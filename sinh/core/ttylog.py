# ttylog - serial device logger
import struct, sys

OP_OPEN, OP_CLOSE, OP_WRITE, OP_EXEC = 1, 2, 3, 4
TYPE_INPUT, TYPE_OUTPUT, TYPE_INTERACT = 1, 2, 3


def ttylog_write(logfile, len, direction, stamp, data=None):
    """This  program  writes  everything  comes  from  a  serial  device"""
    f = file(logfile, 'ab')
    sec, usec = int(stamp), int(1000000 * (stamp - int(stamp)))
    f.write(struct.pack('<iLiiLL', 3, 0, len, direction, sec, usec))
    f.write(data)
    f.close()


def ttylog_open(logfile, stamp):
    f = file(logfile, 'ab')
    sec, usec = int(stamp), int(1000000 * (stamp - int(stamp)))
    f.write(struct.pack('<iLiiLL', 1, 0, 0, 0, sec, usec))
    f.close()


def ttylog_close(logfile, stamp):
    f = file(logfile, 'ab')
    sec, usec = int(stamp), int(1000000 * (stamp - int(stamp)))
    f.write(struct.pack('<iLiiLL', 2, 0, 0, 0, sec, usec))
    f.close()
