#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import scons
from pisi.actionsapi import get

WorkDir = "libffado-2.1.0"

def build():
    scons.make('PREFIX=/usr \
                COMPILE_FLAGS="%s %s" \
                BUILD_TESTS=0' % (get.CXXFLAGS(), get.LDFLAGS()))

def install():
    scons.install("install WILL_DEAL_WITH_XDG_MYSELF=1 DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/usr/share/applications")
    pisitools.dosym("/usr/share/libffado/icons/hi64-apps-ffado.png", "/usr/share/pixmaps/ffado-mixer.png")

    pisitools.dodoc("AUTHORS", "ChangeLog", "LICENSE*", "TODO", "README")
