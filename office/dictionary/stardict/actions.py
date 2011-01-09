#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    shelltools.export("PKG_CONFIG", "/usr/bin/pkg-config")
    autotools.autoreconf("-fiv")
    # shelltools.export("LDFLAGS", "%s -Wl,-z,defs" % get.LDFLAGS())
    shelltools.system("./autogen.sh")

    autotools.configure("--disable-spell \
                         --disable-espeak \
                         --disable-festival \
                         --disable-gucharmap") # \
                         #--disable-schemas-install")

def build():
    # a workaround for ldflags. will be fixed.
    import os
    makefiles=os.popen('find . -name Makefile').read().split()
    for m in makefiles:
        pisitools.dosed(m, r'(^LDFLAGS\s*=.*)', '\\1 -lglib-2.0 -lgtk-x11-2.0 -lpango-1.0 -lORBit-2')
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("usr/share/pixmaps/stardict.png")
    pisitools.remove("usr/share/stardict/pixmaps/docklet_scan.png")
    pisitools.remove("usr/share/stardict/pixmaps/docklet_stop.png")
    pisitools.remove("usr/share/stardict/pixmaps/docklet_normal.png")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO","doc/HowToCreateDictionary")
