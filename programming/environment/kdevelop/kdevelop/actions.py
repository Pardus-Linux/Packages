#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 - 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

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
    pisitools.dodoc("COPYING*","README*","ChangeLog", "AUTHORS", "BUGS", "FAQ", "HACKING*", "NEWS")
    #locales sl and th are very incomplete
    pisitools.removeDir(destinationDirectory="/usr/share/locale/sl")
    pisitools.removeDir(destinationDirectory="/usr/share/locale/th")
