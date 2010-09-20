#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

NoStrip=["/usr/share", "/usr/man"]
WorkDir="krusader-%s" % get.srcVERSION().replace("_","-")
shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure(installPrefix="/usr", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.cd("..")
    pisitools.dosym("/usr/share/icons/hicolor/48x48/apps/krusader_user.png", "/usr/share/icons/hicolor/48x48/apps/krusader.png")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README", "FAQ")
