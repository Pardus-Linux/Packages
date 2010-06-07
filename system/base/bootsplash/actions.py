#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def build():
    shelltools.cd("Utilities/")
    pisitools.dosed("Makefile", "^LDFLAGS.*$", "LDFLAGS = -L$(LIBDIR) %s" % get.LDFLAGS())
    autotools.make()

def install():
    pisitools.dosbin("Utilities/fbmngplay")
    pisitools.dosbin("Utilities/fbtruetype")

    pisitools.dosbin("Utilities/splash", "/sbin")
    pisitools.dosbin("Utilities/splashpbm", "/sbin")
    pisitools.dosbin("Utilities/fbresolution", "/sbin")
