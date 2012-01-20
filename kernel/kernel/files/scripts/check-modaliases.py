#!/usr/bin/python
# -*- coding: utf-8 -*-

# Analyze the given kernel for drivers racing for
# the same devices.

import os
import sys

blacklist = ("radeon", "radeonfb", "nouveau", "nvidiafb")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: %s <kernel version>" % sys.argv[0]
        sys.exit(1)

    kver = sys.argv[1]
    alias_file = "/lib/modules/%s/modules.alias" % kver
    aliases = {}

    if os.path.exists(alias_file):
        for alias in open(alias_file, "r").readlines():
            if alias and not alias.startswith("#"):
                modalias, driver = alias.strip().split(" ", 2)[1:]
                if not modalias.startswith(("pci", "usb")):
                    continue
                if driver in blacklist:
                    continue
                try:
                    aliases[modalias].add(driver)
                except KeyError:
                    aliases[modalias] = set([driver])

    # Dump results
    for modalias, drivers in aliases.items():
        if len(drivers) > 1:
            # More than 1 driver supports this alias
            print "%s: " % modalias,
            print ",".join(drivers)


