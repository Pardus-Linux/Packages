#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

ownerships = {
        "/var/run/cups"         : "root:pnp",
        "/var/log/cups"         : "root:pnp",
    }

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    for directory,owners in ownerships.items():
        if os.path.exists(directory):
            os.system("chown %s %s" % (directory, owners))
