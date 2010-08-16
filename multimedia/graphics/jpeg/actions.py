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

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--enable-shared \
                         --disable-static \
                         --enable-maxmem=64 \
                         --disable-dependency-tracking")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    # they say some programs use this
    pisitools.insinto("/usr/include", "jpegint.h")
    pisitools.insinto("/usr/include", "jinclude.h")

    pisitools.dodoc("change.log", "example.c", "README","*.txt")

