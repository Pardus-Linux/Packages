#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2008-2009  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import scons
from pisi.actionsapi import get

def build():
    scons.make("PREFIX=/usr FAKE_ROOT=%s" % get.installDIR())

def install():
    scons.install()

    pisitools.dosym("/usr/share/linuxdcpp/pixmaps/linuxdcpp.png", "/usr/share/pixmaps/linuxdcpp.png")

    pisitools.dodoc("Changelog.txt", "Credits.txt", "License.txt", "Readme.txt")
