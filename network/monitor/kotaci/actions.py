#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import qt4

def setup():
    qt4.configure()

def build():
    qt4.make()

def install():
    pisitools.dobin("bin/kotaci")
    pisitools.insinto("/usr/share/applications", "data/kotaci.desktop")

    pisitools.insinto("/usr/share/pixmaps", "data/icons/kotaci.png")

    pisitools.dodoc("AUTHORS", "COPYING", "README", "TODO")
