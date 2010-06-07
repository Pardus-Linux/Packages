#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # Suggested C(XX)FLAGS by the upstream author
    shelltools.export("CFLAGS","%s -O3 -fomit-frame-pointer -funroll-loops" % get.CFLAGS())
    shelltools.export("CXXFLAGS","%s -O3 -fomit-frame-pointer -funroll-loops" % get.CXXFLAGS())

    autotools.configure("--disable-static \
                         --with-pic")

    # Remove RPATH
    pisitools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "hardcode_libdir_flag_spec=\"\"")
    pisitools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.doman("lzma.1")
    pisitools.dodoc("AUTHORS","ChangeLog","COPYING*","NEWS","README")
