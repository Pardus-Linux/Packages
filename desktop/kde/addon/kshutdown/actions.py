#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import kde4
from pisi.actionsapi import pisitools

WorkDir = "kshutdown-%s" % get.srcVERSION().replace('_','')
shelltools.export("HOME", "%s" % get.workDIR())

def setup():
    kde4.configure()

def build():
    kde4.make()

def install():
    kde4.install()

    pisitools.dosym("/usr/share/icons/hicolor/64x64/apps/kshutdown.png", "/usr/share/pixmaps/kshutdown.png")

    pisitools.dodoc("LICENSE",  "ChangeLog", "TODO")
    pisitools.dohtml("README.html")
