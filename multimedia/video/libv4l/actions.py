#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

# Raw building
args = "PREFIX=/usr \
        CFLAGS='%s'" % get.CFLAGS().replace("-O2", "-O3")

if get.buildTYPE() == "emul32":
    args += " -C lib LIBDIR=/usr/lib32"
    shelltools.export("CC", "%s -m32" % get.CC())
    shelltools.export("CXX", "%s -m32" % get.CXX())
    #shelltools.export("LDFLAGS", "%s -m32" % get.LDFLAGS())
else:
    args += " LIBDIR=/usr/lib"

def build():
    autotools.make(args)

def install():
    autotools.rawInstall("%s DESTDIR=%s" % (args, get.installDIR()))

    pisitools.dodoc("ChangeLog", "COPYING*", "README*", "TODO")
    pisitools.insinto("/%s/%s/" % (get.docDIR(), get.srcNAME()), "contrib")

