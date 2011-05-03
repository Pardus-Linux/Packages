#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    autotools.autoreconf("-vfi")
    options = "--enable-shared \
               --disable-static \
               --enable-maxmem=64 \
               --disable-dependency-tracking"

    if get.buildTYPE() == "emul32":
        options += " --prefix=/emul32 --libdir=/usr/lib32"
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())

    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/emul32")
        return

    # they say some programs use this
    pisitools.insinto("/usr/include", "jpegint.h")
    pisitools.insinto("/usr/include", "jinclude.h")

    pisitools.dodoc("change.log", "example.c", "README","*.txt")

