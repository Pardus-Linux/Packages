#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = "%s-4.11.2-snapshot-c93f5da3d4e4" % get.srcNAME()
NoStrip=["/"]

def setup():
    pythonmodules.run('configure.py \
                       -b /usr/bin \
                       -d /usr/lib/%s/site-packages \
                       -e /usr/include/%s \
                       CFLAGS+="%s" CXXFLAGS+="%s"' % (get.curPYTHON(), get.curPYTHON(), get.CFLAGS(), get.CXXFLAGS()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("LICENSE*", "NEWS", "README")
