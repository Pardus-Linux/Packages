#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get


WorkDir = "urwid-%s" % get.srcVERSION()
exampledir = "%s/%s/examples" % (get.docDIR(), get.srcNAME())

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
    pisitools.dohtml("*.html")
    pisitools.dodoc("CHANGELOG")

    examples = filter(lambda x: not (x.startswith("docgen") or x == "setup.py"), shelltools.ls("*.py"))
    for f in examples:
        pisitools.insinto(exampledir, f)

    shelltools.chmod("%s/%s/*" % (get.installDIR(), exampledir), 0644)

