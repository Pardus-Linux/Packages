#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "ogdi-3.2.0.beta2"

shelltools.export("TOPDIR", "%s/%s" % (get.workDIR(), WorkDir))

def setup():
    autotools.configure('--with-zlib \
                         --with-projlib="-L/usr/lib -lproj" \
                         --with-expat')

def build():
    shelltools.export("TARGET", "Linux")
    shelltools.export("CFG", "release")
    shelltools.export("LD_LIBRARY_PATH", "%s/%s/bin/linux" % (get.workDIR(),get.srcDIR()))
    autotools.make("-j1")

def install():
    pisitools.dolib_so("bin/Linux/*.so")
    for i in ["gltpd", "ogdi_import", "ogdi_info"]:
        pisitools.dobin("bin/Linux/%s" % i)

    pisitools.insinto("/usr/include", "ogdi/include/*.h")

    pisitools.dosym("/usr/lib/libogdi.so", "/usr/lib/libogdi.so.3")
    # pisitools.dosym("/usr/lib/Linux/libogdi.so", "/usr/lib/libogdi.so.3")

    pisitools.dodoc("ChangeLog", "NEWS", "README")

