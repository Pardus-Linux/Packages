#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "opengfx-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/share/openttd/data", "*.grf")
    pisitools.insinto("/usr/share/openttd/data", "*.obg")
    pisitools.dodoc("*.txt")

