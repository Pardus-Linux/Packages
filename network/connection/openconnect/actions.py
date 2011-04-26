# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make("OPT_FLAGS='%s' openconnect" % get.CFLAGS())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s LIBDIR=/usr/lib" % get.installDIR(), "install-lib")

    pisitools.doman("openconnect.8")

    pisitools.dodoc("AUTHORS", "COPYING*", "README*")
