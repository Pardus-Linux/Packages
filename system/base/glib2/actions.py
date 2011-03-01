#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools


def setup():
    options = "--disable-gtk-doc \
               --with-pcre=system \
               --disable-fam \
               --disable-static \
               --disable-systemtap"


    if get.buildTYPE() == "emul32":
        options += " --prefix=/emul32 \
                     --libdir=/usr/lib32 \
                     --disable-dtrace"
        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("PKG_CONFIG_LIBDIR", "/usr/lib32/pkgconfig")

    autotools.autoreconf("-vif")
    autotools.configure(options)

    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        pisitools.domove("/emul32/bin/gio-querymodules", "/usr/bin/32/")
        pisitools.removeDir("/emul32")

    pisitools.removeDir("/usr/share/gtk-doc")
    pisitools.removeDir("/usr/share/gdb")

    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "NEWS")
