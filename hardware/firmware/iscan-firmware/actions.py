#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."
NoStrip = ["/"]

def install():
    libdir = "usr/lib%s" % ("64" if get.ARCH() == "x86_64" else "")

    pisitools.insinto("/usr/lib/iscan", "%s/iscan/*" % libdir)
    pisitools.insinto("/usr/lib/esci", "%s/esci/*" % libdir)

    pisitools.insinto("/usr/share/esci", "usr/share/esci/*")
    pisitools.insinto("/usr/share/iscan", "usr/share/iscan/*")
    pisitools.insinto("/usr/share/iscan-data/device", "usr/share/iscan-data/device/*")

    pisitools.insinto("/usr/share/doc/%s" % get.srcNAME(), "usr/share/doc/*")

    # Dodoc one of the plugins doc files, it's all same.
    for d in shelltools.ls("iscan-plugin-gt-f520/usr/share/doc/iscan-plugin-gt-f520-1.0.0"):
        pisitools.dodoc("iscan-plugin-gt-f520/usr/share/doc/iscan-plugin-gt-f520-1.0.0/%s" % d)
