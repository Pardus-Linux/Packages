#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

patches = []
all_patches = os.popen("find files/ -name '*.patch'").read().strip().split("\n")

def is_avail(patch):
    for p in all_patches:
        if patch in p:
            return p

for line in open(sys.argv[1], "r").readlines():
    if not line.strip().startswith("#") and ("ApplyPatch" in line or "ApplyOptionalPatch" in line):
        try:
            patch = line.strip().split()[1]
            p = os.path.join(os.path.dirname(sys.argv[1]), patch)
            if os.path.exists(p) and not is_avail(patch):
                patches.append("%s %s" % (str(os.stat(p).st_size), patch ))
        except:
            pass

patches.sort(cmp=lambda x,y: int(x.split()[0])-int(y.split()[0]))
print "\n".join(patches)
