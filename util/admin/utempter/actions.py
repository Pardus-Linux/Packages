#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.export("LDFLAGS", "%s -Wl,-z,now" % get.LDFLAGS())

    autotools.make('RPM_OPT_FLAGS="%s"' % get.CFLAGS())

def install():
    autotools.rawInstall('RPM_BUILD_ROOT="%s" LIBDIR=/usr/lib' % get.installDIR())
    pisitools.dobin("utmp")
