#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "unsermake"
destdir = "/usr/share/unsermake"

def install():
    pisitools.dodir(destdir)

    for f in shelltools.ls("./"):
        if f.endswith(".py") or f.endswith(".um"):
            shelltools.chmod(f, 0644)
            pisitools.insinto(destdir, f)

    shelltools.chmod("unsermake", 0755)
    pisitools.insinto(destdir, "unsermake")

    pisitools.dodoc("COPYING", "README", "TODO")

