#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (c) TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--with-svgz \
                         --with-croco \
                         --disable-gtk-doc \
                         --disable-gnome-print \
                         --disable-static")

def build():
    autotools.make()

def install():
    pisitools.dodir("/etc/gtk-2.0/")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/gtk-doc")

    pisitools.dodoc("COPYING", "AUTHORS", "ChangeLog", "README")
