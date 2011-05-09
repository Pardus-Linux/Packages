#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install("--root %s" % get.installDIR())

    pisitools.dodoc("COPYING", "NEWS", "PKG-INFO", "README")
    pisitools.doman("docs/buildslave.1")

    pisitools.dodir("/var/lib/buildslave")
