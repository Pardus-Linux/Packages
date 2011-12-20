#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "%s -D_GNU_SOURCE" % get.CFLAGS())
    autotools.aclocal("-I gnulib/m4 -I m4")
    autotools.automake()
    shelltools.touch("configure")
    shelltools.touch("config.h")

    autotools.configure("--enable-nls \
                         --without-included-regex \
                         --disable-rpath \
                         --disable-assert \
                         --with-fts \
                         --enable-leaf-optimisation \
                         --enable-d_type-optimization")

def build():
    autotools.make()

# Sandbox ihlali: rmdir (/// -> /)
def check():
    autotools.make("check")

def install():
    autotools.install()

    pisitools.dodoc("ChangeLog", "NEWS", "TODO", "README")
