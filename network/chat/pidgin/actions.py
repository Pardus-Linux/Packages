#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import perlmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS","%s -fstack-protector-all" % get.CFLAGS())

    autotools.autoreconf("-vfi")
    autotools.configure("--enable-dbus \
                         --enable-cyrus-sasl \
                         --enable-gnutls=yes \
                         --enable-nss=no \
                         --enable-cap \
                         --disable-schemas-install \
                         --disable-meanwhile \
                         --enable-nm \
                         --disable-tcl \
                         --disable-tk \
                         --x-includes=/usr/include/X11 \
                         --with-gnutls-includes=/usr/include/gnutls \
                         --with-gnutls-libs=/usr/lib")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "HACKING", "NEWS", "README", "ChangeLog")
