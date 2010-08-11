#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import sys
import pisi

oldwd = os.getcwd()
repo_root = "/root/2009/"

kpspec = pisi.specfile.SpecFile('pspec.xml')
kver = kpspec.history[0].version

if len(sys.argv) == 3:
    repo_root = sys.argv[1]
    krel = sys.argv[2]
else:
    krel = kpspec.history[0].release

for d in ["devel"]:
    os.chdir(repo_root+d)

    packages = os.popen("grep --exclude=pisi-index* --exclude-dir=.svn -r '<Dependency release=\".*\">kernel.*' * | gawk -F: '{ print $1 }'").read().strip().split()

    for p in packages:
        a = re.sub("<Dependency release=\".*\">(kernel.*)", "<Dependency release=\"%s\">\\1" % krel, open(p, "r").read())
        open(p, "w").write(a)

os.chdir(oldwd)
