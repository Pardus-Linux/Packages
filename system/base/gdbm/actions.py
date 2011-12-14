#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static \
                         --enable-libgdbm-compat")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/usr/include/gdbm")
    pisitools.dosym("../gdbm.h", "/usr/include/gdbm/gdbm.h")
    pisitools.dosym("../ndbm.h", "/usr/include/gdbm/ndbm.h")
    pisitools.dosym("../dbm.h", "/usr/include/gdbm/dbm.h")

    pisitools.dodoc("ChangeLog", "NEWS", "README")
