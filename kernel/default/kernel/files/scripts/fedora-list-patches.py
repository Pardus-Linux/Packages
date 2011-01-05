#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

from hashlib import md5

(SIZE, ALREADYINSPEC, DIFF) = range(3)

def files_are_same(filea, fileb):
    md5a = md5(open(filea, "r").read())
    md5b = md5(open(fileb, "r").read())

    return md5a.hexdigest() == md5b.hexdigest()

def usage():
    print "%s <path to RPM spec> [--different|--new]" % sys.argv[0]
    return 1

if __name__ == "__main__":

    patches = {}
    rpm = None
    try:
        rpm = sys.argv[1]
    except IndexError:
        sys.exit(usage())

    dirname = os.path.dirname(rpm)

    for line in open(rpm, "r").readlines():
        line = line.strip()
        if not line.startswith("#") and \
            line.startswith(("ApplyPatch", "ApplyOptionalPatch")) and \
            "()" not in line:
            fedora_patch_name = line.split()[1]
            fedora_patch_file = os.path.join(dirname, fedora_patch_name)
            if os.path.exists(fedora_patch_file):
                pspec_patch_file = os.path.join("files/patches/fedora", fedora_patch_name)
                if not os.path.exists(pspec_patch_file):
                    patches[fedora_patch_name] = (str(os.stat(fedora_patch_file).st_size),
                                                  False,
                                                  False)
                else:
                    patches[fedora_patch_name] = (str(os.stat(fedora_patch_file).st_size),
                                                  os.path.exists(pspec_patch_file),
                                                  not files_are_same(fedora_patch_file, pspec_patch_file))


    for patch, stats in patches.items():
        if stats[DIFF]:
            print "M %10s  %s" % (stats[SIZE], patch)
        elif not stats[ALREADYINSPEC]:
            # New patches
            print "? %10s  %s" % (stats[SIZE], patch)

