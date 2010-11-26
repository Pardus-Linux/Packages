#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # Libs should be installed to /lib because it's possible that /usr
    # is on a different partition other than rootfs.
    autotools.autoreconf("-fi")
    autotools.configure("--sbindir=/sbin \
                         --libdir=/lib \
                         --disable-rpath")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.domove("/lib/pkgconfig", "/usr/lib")

    pisitools.dodoc("COPYING", "ChangeLog", "AUTHORS", "TODO")
