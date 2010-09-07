#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "cfitsio"

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static")

def build():
    autotools.make("shared")

    for t in ("fpack", "funpack", "imcopy", "fitscopy", "listhead"):
        autotools.make(t)

    pisitools.dosed("cfitsio.pc", "\\$\\{prefix\\}/include", "${prefix}/include/%s" % get.srcNAME())

def install():
    for t in ("fpack", "funpack", "imcopy", "fitscopy", "listhead"):
        pisitools.dobin(t)

    autotools.rawInstall("DESTDIR=%s LIBDIR=/usr/lib INCLUDEDIR=include/%s CFITSIO_LIB=%s/usr/lib CFITSIO_INCLUDE=%s/usr/include/%s" % (get.installDIR(), get.srcNAME(), get.installDIR(), get.installDIR(), get.srcNAME()))

    pisitools.remove("/usr/lib/*.a")

    pisitools.domove("/usr/lib/libcfitsio.so", "/usr/lib", "libcfitsio.so.0.0")
    pisitools.dosym("/usr/lib/libcfitsio.so.0.0", "/usr/lib/libcfitsio.so.0")
    pisitools.dosym("/usr/lib/libcfitsio.so.0.0", "/usr/lib/libcfitsio.so")

    pisitools.dodoc("*.txt", "README")
