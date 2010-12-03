#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "nuvola"

def install():
    pisitools.dodir("/usr/share/icons/Nuvola")

    for dir in ("128x128", "64x64", "48x48", "32x32", "22x22", "16x16", "extra", "scalable"):
        shelltools.copytree(dir, "%s/usr/share/icons/Nuvola/%s" % (get.installDIR(), dir))

    pisitools.insinto("/usr/share/icons/Nuvola", "author.txt")
    pisitools.insinto("/usr/share/icons/Nuvola", "index.theme")
    pisitools.insinto("/usr/share/icons/Nuvola", "license.txt")
    pisitools.insinto("/usr/share/icons/Nuvola", "readme.txt")
