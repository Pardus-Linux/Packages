#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "mjpegtools-%s" % get.srcVERSION().replace("_", "")

def setup():
    shelltools.export("CFLAGS", "%s -fno-strict-aliasing" % get.CFLAGS())
    autotools.autoreconf("-vfi")

    pisitools.dosed("configure", "ARCHFLAGS=.*", "ARCHFLAGS=")
    autotools.configure("--with-x \
                         --enable-largefile \
                         --enable-simd-accel \
                         --with-dv-yv12 \
                         --disable-static \
                         --with-libpng \
                         --with-libdv=/usr")


def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS","ChangeLog","README*","mjpeg_howto.txt", "TODO")
