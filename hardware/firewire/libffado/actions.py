#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import scons
from pisi.actionsapi import get

WorkDir = "%s" % get.srcDIR().replace("_", "-")

def build():
    pisitools.dosed("SConstruct", "usr/local", "usr")
    scons.make()

def install():
    scons.install("install DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/usr/share/applications")
    pisitools.dosym("/usr/share/libffado/icons/hi64-apps-ffado.png", "/usr/share/pixmaps/ffado-mixer.png")

    pisitools.dodoc("AUTHORS", "ChangeLog", "LICENSE*", "TODO", "README")
