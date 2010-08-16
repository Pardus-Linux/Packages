#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "xz-4.999.9beta-143-g3e49"

def setup():
    # Suggested C(XX)FLAGS by the upstream author
    shelltools.export("CFLAGS", "%s -D_FILE_OFFSET_BITS=64" % get.CFLAGS())
    shelltools.export("CXXFLAGS", "%s -D_FILE_OFFSET_BITS=64" % get.CXXFLAGS())

    autotools.configure("--disable-static \
                         --disable-rpath")

    # Fix overlinking
    pisitools.dosed("libtool", "-pthread", "-lpthread")

    # Remove RPATH
    pisitools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "hardcode_libdir_flag_spec=\"\"")
    pisitools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")

def build():
    autotools.make()

def check():
    shelltools.export("LD_LIBRARY_PATH", "%s/src/liblzma/.libs" % get.curDIR())
    autotools.make("check")

def install():
    autotools.install()

    pisitools.remove("/usr/share/man/man1/lzmadec.1")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README")
