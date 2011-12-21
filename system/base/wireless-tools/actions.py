#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile", "CC = .*", "CC = %s" % get.CC())

def build():
    autotools.make("OPT_FLAGS='%s' FORCE_WEXT_VERSION=16 BUILD_SHARED=1" % get.CFLAGS())

def install():
    autotools.rawInstall("PREFIX=%s/usr \
                          INSTALL_LIB=%s/usr/lib \
                          INSTALL_INC=%s/usr/include \
                          INSTALL_MAN=%s/usr/share/man" % ((get.installDIR(),)*4))

    pisitools.dodoc("COPYING", "README")
