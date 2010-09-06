#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DPODOFO_BUILD_SHARED=1 \
            -DPODOFO_BUILD_STATIC=0 \
            -DWANT_BOOST=1 \
            -DUSE_STLPORT=1")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "COPYING.LIB", "ChangeLog", "NEWS", "TODO")
    pisitools.dohtml("README.html", "FAQ.html")
