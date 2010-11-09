#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="ATLAS"

bits = {"i686"  : "32",
        "x86_64": "64"}

def setup():
    pisitools.dosed("configure", "cc=gcc", "cc=%s" % get.CC())
    pisitools.dosed("configure", 'cflags="-g.*', "cflags=%s" % get.CFLAGS())

    shelltools.makedirs("build")
    shelltools.cd("build")

    shelltools.system("../configure \
                       -Si cputhrchk 0 \
                       -Fa alg -fPIC \
                       -b %s \
                       --with-netlib-lapack=/usr/lib/liblapack.a" % bits[get.ARCH()])

    # Fix architecture detection
    if get.ARCH() == "x86_64":
        pisitools.dosed("Make.inc", "ARCH =.*", "ARCH = HAMMER64SSE2")
        pisitools.dosed("Make.inc", "-DATL_SSE3", "")
        pisitools.dosed("Make.inc", "-msse3", "-msse2")
    elif get.ARCH() == "i686":
        pisitools.dosed("Make.inc", "ARCH =.*", "ARCH = PIII32SSE1")
        pisitools.dosed("Make.inc", "-DATL_SSE3 -DATL_SSE2", "")
        pisitools.dosed("Make.inc", "-msse3", "-msse")


def build():
    autotools.make("-C build -j1")
    autotools.make("-C build/lib shared")

def install():
    for lib in ["atlas","cblas","f77blas"]:
        pisitools.dolib("build/lib/lib%s.so" % lib)

    for header in ["cblas.h","clapack.h"]:
        pisitools.insinto("/usr/include", "include/%s" % header)

    pisitools.dodoc("README","doc/*")
