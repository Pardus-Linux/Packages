#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("m4")
    shelltools.makedirs("contrib/minizip/m4")

    shelltools.copy("minigzip.c", "contrib/minizip")

    autotools.rawConfigure("--libdir=/usr/lib \
                            --includedir=/usr/include \
                            --prefix=/usr")

def build():
    autotools.make()

    shelltools.cd("contrib/minizip")
    autotools.autoreconf("-vi")

    autotools.configure()
    autotools.make()

def check():
    autotools.make("test")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Copy zlib to /lib
    pisitools.remove("/usr/lib/*.a")
    pisitools.domove("/usr/lib/libz*", "/lib")

    # Create symlinks in /usr/lib
    pisitools.dosym("/lib/libz.so.%s" % get.srcVERSION(), "/usr/lib/libz.so.%s" % get.srcVERSION())
    pisitools.dosym("libz.so.%s" % get.srcVERSION(), "/usr/lib/libz.so.1")
    pisitools.dosym("libz.so.1", "/usr/lib/libz.so")

    # Install minizip
    autotools.rawInstall("-C contrib/minizip DESTDIR=%s" % get.installDIR())

    pisitools.doman("zlib.3")
    pisitools.dodoc("FAQ", "README", "ChangeLog", "doc/algorithm.txt", "example.c")

