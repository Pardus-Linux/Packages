#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import kerneltools
from pisi.actionsapi import get

WorkDir = "vloopback-%s" % get.srcVERSION()
KVER = kerneltools.getKernelVersion()

def setup():
    pisitools.dosed("Makefile", "SUBDIRS=", "M=")
    pisitools.dosed("Makefile", "\$\(shell uname -r\)", KVER)
    shelltools.chmod("example/*", 0644)

def build():
    autotools.make("KERNELDIR=/lib/modules/%s/build default" % KVER)

def install():
    pisitools.insinto("/lib/modules/%s/extra" % KVER, "*.ko")
    pisitools.insinto("%s/%s/" % (get.docDIR(), get.srcNAME()), "example")

    pisitools.dodoc("COPYING", "README")
    pisitools.dohtml("*.html")

