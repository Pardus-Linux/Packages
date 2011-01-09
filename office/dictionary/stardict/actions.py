#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    shelltools.export("PKG_CONFIG", "/usr/bin/pkg-config")
    shelltools.system("./autogen.sh")
    # autotools.autoreconf("fiv")
    autotools.configure("--prefix=/usr \
                         --disable-gnome \
                         --disable-spell \
                         --disable-espeak \
                         --disable-festival \
                         --disable-gucharmap \
                         --disable-gucharmap \
                         --disable-schemas-install")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("usr/share/pixmaps/stardict.png")
    pisitools.remove("usr/share/stardict/pixmaps/docklet_scan.png")
    pisitools.remove("usr/share/stardict/pixmaps/docklet_stop.png")
    pisitools.remove("usr/share/stardict/pixmaps/docklet_normal.png")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO","doc/HowToCreateDictionary")
