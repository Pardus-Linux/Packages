#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    shelltools.export("OS_CFLAGS", get.CFLAGS())
    shelltools.export("OS_LDFLAGS", get.LDFLAGS())
    shelltools.export("OS_CXXFLAGS", get.CXXFLAGS())

    autotools.make()

def install():
    autotools.install("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/cups/model/samsung/cms", "cms/*")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README", "THANKS", "TODO")
