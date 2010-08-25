#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get


WorkDir = "%s-%s" % (get.srcNAME(), get.srcVERSION().replace("_", "-"))

def setup():
    shelltools.sym(".", "m4")
    shelltools.export("CFLAGS", "%s -DDRV_RAW" % get.CFLAGS())

    autotools.autoreconf("-vfi -Im4")
    libtools.gnuconfig_update()
    autotools.configure("--disable-esd \
                         --disable-af \
                         --disable-alsa \
                         --enable-oss \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "NEWS", "README", "TODO")
    pisitools.dohtml("docs/*.html")

