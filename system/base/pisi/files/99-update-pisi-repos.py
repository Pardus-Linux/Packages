#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import fcntl

import comar

LOCK_FILE = "/var/lock/subsys/pisi"

if __name__ == "__main__":
    if sys.argv[2] != "up":
        sys.exit(0)

    try:
        lock = open(LOCK_FILE, "w")
    except IOError:
        sys.exit(0)

    try:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except IOError:
        sys.exit(0)

    link = comar.Link()

    lock.close()
    link.System.Manager["pisi"].updateAllRepositories()
