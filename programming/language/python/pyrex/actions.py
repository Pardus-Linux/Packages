#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

WorkDir = "Pyrex-%s" % get.srcVERSION()

def install():
    pythonmodules.install()

    pisitools.dodoc("CHANGES.txt", "README.txt", "USAGE.txt")
    pisitools.dohtml("Doc/*")
