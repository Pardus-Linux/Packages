#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

os.system("svn up")
lastrev = os.popen("svn info | grep 'Last Changed Rev'").read().strip().split("Last Changed Rev: ")[1]

for k in ["pae"]:
    wd = os.getcwd()
    dir = os.path.join("../../", "%s/kernel-%s" % (k, k))
    os.chdir(dir)
    os.system("svn up")
    os.system("svn merge -c %s %s ." % (lastrev, wd))
    os.system("svn ci -m \"%s\"" % sys.argv[1])
