#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="adjustableclock-%s" % get.srcVERSION()
shelltools.export("HOME", "%s" % get.workDIR())

def setup():
    cmaketools.configure(installPrefix="/usr/kde/4", sourceDir=".")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "COPYING", "CHANGELOG")
