#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir ="icecc-%s" % get.srcVERSION()

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--prefix=/opt/icecream \
                         --localstatedir=/var \
                         --disable-static \
                         --enable-shared")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for chost in ["", "%s-pc-linux-gnu-" % get.ARCH()]:
        for i in ["c++", "cc", "g++", "gcc"]:
            pisitools.dosym("icecc", "/opt/icecream/bin/%s%s" % (chost, i))
