#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "widelands-build15-src"

def setup():
    shelltools.makedirs("build-cmake")
    shelltools.cd("build-cmake")
    cmaketools.configure(sourceDir="..")

def build():
    shelltools.cd("build-cmake")
    cmaketools.make()

def install():
    shelltools.cd("build-cmake")
    cmaketools.install()

    shelltools.cd("..")
    datadirs = ["campaigns", "fonts", "global", "maps", "music", "pics", "scenario_examples", "sound", "tribes", "txts", "worlds"]
    for dir in datadirs:
        shelltools.copytree(dir, "%s/usr/share/widelands" % get.installDIR())

    pisitools.dodoc("COPYING", "CREDITS", "ChangeLog")
