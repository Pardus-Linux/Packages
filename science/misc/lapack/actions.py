#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    shelltools.copy("INSTALL/make.inc.gfortran", "make.inc")

    if get.ARCH() == "x86_64":
        pisitools.dosed("make.inc", "-O2", "%s -fPIC -m64 -funroll-all-loops" % get.CFLAGS())
        pisitools.dosed("make.inc", "NOOPT    =", "NOOPT    =-m64 -fPIC ")
    else:
        pisitools.dosed("make.inc", "-O2", "%s -fPIC -funroll-all-loops" % get.CFLAGS())

def build():
    autotools.make("-j1")

def install():
    pisitools.insinto("/usr/lib","SRC/liblapack.*")
    pisitools.insinto("/usr/lib","BLAS/SRC/libblas.*")

    pisitools.insinto("/usr/lib","lapack_LINUX.a","liblapack.a")
    pisitools.insinto("/usr/lib","blas_LINUX.a","libblas.a")

    pisitools.dodoc("LICENSE", "README")
