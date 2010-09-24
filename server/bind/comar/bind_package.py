#!/usr/bin/python

import os

UID = "named"
GID = "named"

directories = ("/var/named", "/var/run/named")

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if not os.path.exists("/etc/bind/rndc.key"):
        os.system("/usr/sbin/rndc-confgen -r /dev/urandom -a -u named")

    # Ownerships
    for d in directories:
        os.system("chown %s:%s %s" % (UID, GID, d))
