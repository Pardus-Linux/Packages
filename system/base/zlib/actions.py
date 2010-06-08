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
    autotools.autoreconf("-fi")

    autotools.configure("--disable-static")


def build():
    autotools.make()

def install():
    autotools.install()

    # Copy zlib to /lib
    pisitools.domove("/usr/lib/libz*", "/lib")

    # Create symlinks in /usr/lib
    pisitools.dosym("/lib/libz.so.%s" % get.srcVERSION(), "/usr/lib/libz.so.%s" % get.srcVERSION())
    pisitools.dosym("libz.so.%s" % get.srcVERSION(), "/usr/lib/libz.so.1")
    pisitools.dosym("libz.so.1", "/usr/lib/libz.so")

    for header in ["zconf.h","zlib.h","zutil.h"]:
        pisitools.insinto("/usr/include", header)

    pisitools.doman("zlib.3")
    pisitools.dodoc("FAQ", "README", "ChangeLog", "algorithm.txt")

