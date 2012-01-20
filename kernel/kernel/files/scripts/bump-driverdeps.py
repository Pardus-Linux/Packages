#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import sys
import pisi
import time

PACKAGER = "YOUR NAME"
PACKAGER_EMAIL = "YOUR EMAIL"

RELEASE = """\
        <Update release="%s">
            <Date>%s</Date>
            <Version>%s</Version>
            <Comment>Bump release for new kernel.</Comment>
            <Name>%s</Name>
            <Email>%s</Email>
        </Update>
"""

def increment_release(pspec, krel):
    last_history = pisi.specfile.SpecFile(pspec).history[0]
    release = int(last_history.release)+1
    ver = last_history.version
    date = time.strftime("%Y-%m-%d")

    global RELEASE
    new_release = RELEASE % (release, date, ver, PACKAGER, PACKAGER_EMAIL)

    # Update dependency releases if any
    newpspec = re.sub('\<Dependency version=".*"\>(kernel.*)<', '<Dependency version="%s">\\1<' % krel, open(pspec, "r").read())
    newpspec = newpspec.replace("<History>\n", "<History>\n%s" % new_release)

    open(pspec, "w").write(newpspec)


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print "Usage: %s <new version>" % sys.argv[0]
        sys.exit(1)

    # Check .packagerinfo
    if os.path.exists(os.path.expanduser("~/.packagerinfo")):
        PACKAGER, PACKAGER_EMAIL = open(os.path.expanduser("~/.packagerinfo"), "r").read().strip().split(",")

    krel = sys.argv[1]
    os.chdir("../../")

    packages = os.popen("grep -l --exclude-dir=.svn -r '<Dependency version=\".*\">kernel.*' * | gawk -F: '{ print $1 }'").read().strip().split()

    for p in set(packages):
        print p
        increment_release(p, krel)
