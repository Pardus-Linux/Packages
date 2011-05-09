#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import autotools

docdir = get.docDIR()


def build():
    pythonmodules.compile()
    autotools.make("-C docs buildbot.html")

def install():
    pythonmodules.install("--root %s" % get.installDIR())

    pisitools.doman("docs/buildbot.1")

    # install examples
    pisitools.insinto("%s/buildbot" % docdir, "docs/examples")

    pisitools.dohtml("docs/")

    fileDimensions = ["32", "48","64"]
    for dimension in fileDimensions:
        pisitools.remove("%s/buildbot/html/hexnut%s.png" % (docdir, dimension))

    pisitools.dodir("/var/lib/buildmaster")

