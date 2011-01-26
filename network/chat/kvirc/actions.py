#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "kvirc-4.0rc3"
NoStrip = "/usr/kde/4/share"
shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.unlinkDir("win32build")
    cmaketools.configure(installPrefix="/usr/kde/4", sourceDir=".")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("/usr/share/icons/hicolor/128x128/apps/kvirc.png", "/usr/share/pixmaps/kvirc.png")
    pisitools.domove("/usr/kde/4/share/applications/kvirc.desktop", "/usr/kde/4/share/applications/kde4")
