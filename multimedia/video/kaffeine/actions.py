#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "%s-%s" % (get.srcNAME(), get.srcVERSION().replace("_", "-"))
shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure(installPrefix="/usr/kde/4",sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    pisitools.dodoc("COPYING", "COPYING-DOCS", "Changelog", "NOTES")

    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
