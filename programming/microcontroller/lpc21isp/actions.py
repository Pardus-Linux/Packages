#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "lpc21isp"

def build():
    autotools.make()

def install():
    pisitools.dobin("lpc21isp")
    pisitools.insinto("/usr/include/", "*.h")
    pisitools.dodoc("README", "lgpl-3.0.txt", "gpl.txt")
