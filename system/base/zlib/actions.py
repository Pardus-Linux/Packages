#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

version = get.srcVERSION()

def setup():
    pisitools.dosed("Makefile*", "ldconfig \|\| ", "")

    autotools.rawConfigure("--shared \
                            --prefix=/usr \
                            --libdir=/lib")

def build():
    autotools.make()

def install():
    autotools.install("libdir=%s/lib" % get.installDIR())
    pisitools.dolib("libz.so.%s" % version)

    shelltools.chmod("%s/lib/libz.so.*" % get.installDIR())
    libtools.gen_usr_ldscript("libz.so")

    pisitools.remove("/lib/libz.a")

    for header in ["zconf.h","zlib.h","zutil.h"]:
        pisitools.insinto("/usr/include", header)

    pisitools.doman("zlib.3")
    pisitools.dodoc("FAQ", "README", "ChangeLog", "algorithm.txt")

def test():
    autotools.make("test")

