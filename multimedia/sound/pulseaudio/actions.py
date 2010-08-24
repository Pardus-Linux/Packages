#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import libtools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    # Disable as-needed for now as it doesn't compile
    # Lennart has introduced a circular dep in the libraries. libpulse requires
    # libpulsecommon but libpulsecommon requires libpulse.
    shelltools.export("LDFLAGS", "%s -Wl,--no-as-needed" % get.LDFLAGS())

    autotools.autoreconf("-fi")
    libtools.libtoolize()

    autotools.configure("--disable-dependency-tracking \
                         --disable-static \
                         --disable-rpath \
                         --disable-hal \
                         --localstatedir=/var \
                         --with-system-user=pulse \
                         --with-system-group=pulse \
                         --with-access-group=pulse-access")

def build():
    #autotools.make("LIBTOOL=/usr/bin/libtool")
    autotools.make()

    #generate html docs
    autotools.make("doxygen")

def check():
    # All 29 tests passes, yay
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "LICENSE", "GPL", "LGPL", "todo", "ChangeLog")
    pisitools.dohtml("doxygen/html/*")

    # Needed for service.py
    pisitools.dodir("/var/run/pulse")
    pisitools.dodir("/var/lib/pulse")

    # HAL is no longer supported by default
    pisitools.removeDir("/etc/dbus-1")
