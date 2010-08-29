#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CC", get.CC())
    shelltools.export("CXX", get.CXX())
    shelltools.export("RANLIB", get.RANLIB())
    shelltools.export("AR", get.AR())

    # enable-debug is bogus, it should stay here
    autotools.configure("--with-x \
                         --enable-opengl-player \
                         --disable-gtk-player \
                         --enable-mmx \
                         --disable-assertions \
                         --disable-static \
                         --enable-debug")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("CHANGES", "README*", "TODO")

