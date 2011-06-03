#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export('HOME', get.workDIR())

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--disable-static\
                         --disable-scrollkeeper\
                         --disable-schemas-install\
                         --disable-nautilus \
                         --enable-pixbuf\
                         --enable-t1lib \
                         --enable-comics \
                         --enable-impress")
                        # enable-introspection needs libevdocument installed
                        # so once the package enters the repositories,
                        # we can try enabling introspection
                        # --enable-introspection \

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "COPYING", "TODO", "AUTHORS", "ChangeLog")
