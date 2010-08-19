#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "v4l-utils-%s" % get.srcVERSION()

def build():
    # shelltools.export("CC", get.CC())
    autotools.make('-j1 \
                    PREFIX=/usr \
                    LIBDIR=/usr/lib \
                    CFLAGS="%s"' % get.CFLAGS().replace("-O2", "-O3"))

def install():
    autotools.rawInstall("PREFIX=/usr \
                          LIBDIR=/usr/lib \
                          DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "COPYING*", "README*", "TODO")
