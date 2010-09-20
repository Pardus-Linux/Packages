#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import kde4

shelltools.export("HOME", get.workDIR())

def setup():
    kde4.configure()
    #cmaketools.configure(sourceDir=".")

def build():
    kde4.make()
    #cmaketools.make()

def install():
    kde4.install()
    #cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dosym("/usr/share/icons/hicolor/128x128/apps/reqonk.png", "/usr/share/pixmaps/reqonk.png")

    pisitools.dodoc("COPYING", "AUTHORS", "TODO", "ChangeLog")
