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
    autotools.rawConfigure("--libdir=/usr/lib \
                            --mandir=/usr/share/man \
                            --libexecdir=/usr/lib \
                            --bindir=/usr/bin")
def build():
    autotools.make()

def install():
    autotools.make("DESTDIR=%s install install-lib install-dev" % get.installDIR())

    pisitools.remove("/usr/lib/*.a")
    shelltools.chmod("%s/usr/lib/libattr.so.*.*.*" % get.installDIR(), 0755)

    pisitools.removeDir("/usr/share/doc/attr-*")
    pisitools.dodoc("README", "doc/COPYING")
