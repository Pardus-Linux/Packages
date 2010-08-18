#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "xc/lib/Xaw3d"

def setup():
    shelltools.makedirs("X11")
    shelltools.cd("X11")
    shelltools.system("ln -sf ../../Xaw3d .")
    shelltools.cd("../")
    shelltools.system("xmkmf")

def build():
    autotools.make("-j1 includes")
    autotools.make("-j1 depend")
    autotools.make("-j1 CC=\"%s\" CFLAGS=\"-I. %s\" SHLIBGLOBALSFLAGS=\"%s\"" % (get.CC(), get.CFLAGS(), get.LDFLAGS()))

def install():
    autotools.rawInstall("DESTDIR=%s install" % get.installDIR())

    pisitools.dodoc("README.XAW3D")
