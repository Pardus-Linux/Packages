#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def install():
    perlmodules.install()
    pisitools.insinto("/usr/share/applications", "dvdrip.desktop")
    pisitools.insinto("/usr/share/pixmaps", "lib/Video/DVDRip/icon.xpm", "dvdrip.xpm")

    pisitools.dodoc("Changes*", "COPYRIGHT", "Credits", "README", "TODO")
