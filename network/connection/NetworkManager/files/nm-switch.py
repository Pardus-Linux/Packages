#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import sys

CONFFILE = "/etc/conf.d/NetworkManager"

def usage(progname):
    print "Usage: %s [enable|disable|status]" % progname
    return 1

def switch(cmd):
    new_conf = re.sub("DEFAULT=\".*\"", "DEFAULT=\"%s\"" % ("True" if cmd=="enable" else "False"),
                                        open(CONFFILE).read())
    open(CONFFILE, "w").write(new_conf)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(usage(sys.argv[0]))

    cmd = sys.argv[1]
    if cmd in ("enable", "disable"):
        sys.exit(switch(cmd))
    elif cmd == "status":
        print "COMAR" if re.search('DEFAULT="False"', open(CONFFILE, "r").read().strip()) else "NetworkManager"
        sys.exit(0)
    else:
        sys.exit(usage(sys.argv[0]))
