#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    if get.buildTYPE() == "emul32":
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())

    pisitools.dosed("Make.Rules", "pardusCFLAGS", get.CFLAGS())
    pisitools.dosed("Make.Rules", "pardusLDFLAGS", get.LDFLAGS())

def build():
    args = "emul32=1" if get.buildTYPE() == "emul32" else ""
    autotools.make('CC="%s" %s' % (get.CC(), args))

def install():
    if get.buildTYPE() == "emul32":
        autotools.rawInstall("FAKEROOT=%s \
                              LIBDIR=%s/usr/lib32 \
                              emul32=1" % ((get.installDIR(),)*2))
        pisitools.remove("/usr/lib32/*.a")
        return

    autotools.rawInstall("FAKEROOT=%s" % get.installDIR())

    pisitools.insinto("/etc/security", "pam_cap/capability.conf")

    # we should not need this static
    pisitools.remove("/lib/libcap.a")

    pisitools.dodoc("CHANGELOG", "README", "doc/capability.notes")
