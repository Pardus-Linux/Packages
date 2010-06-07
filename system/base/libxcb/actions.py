#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "%s -DNDEBUG" % get.CFLAGS())

    autotools.autoreconf("-vif")
    autotools.configure("--disable-static \
                         --disable-xevie \
                         --disable-xprint \
                         --without-doxygen")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("COPYING", "NEWS", "README")
