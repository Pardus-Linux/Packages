#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--enable-ffcall \
                        --enable-gnutls \
                        --enable-tls \
                        --enable-zeroconf \
                        --with-default-config=/etc/GNUstep/GNUstep.conf")

def build():
    autotools.make()

    shelltools.export("LD_LIBRARY_PATH", "%s/%s/Source/obj:${LD_LIBRARY_PATH}" % (get.workDIR(), get.srcDIR()))
    autotools.make("-C Documentation")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("-C Documentation")

    pisitools.dodoc("COPYING", "NEWS")
