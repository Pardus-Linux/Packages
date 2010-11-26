#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    shelltools.export("CXXFLAGS", "%s -lcrypto -lpthread" % get.CXXFLAGS())
    shelltools.export("CFLAGS", get.CFLAGS())
    autotools.configure("--sysconfdir=/etc/dcmtk \
                         --with-private-tags")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "install-lib")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "install-include")

    pisitools.dodoc("CHANGES.354")
