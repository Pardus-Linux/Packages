#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.rawConfigure("--libdir=/lib \
                            --mandir=/usr/share/man \
                            --libexecdir=/lib \
                            --bindir=/bin")
def build():
    autotools.make()

def install():
    autotools.make("DESTDIR=%s install install-lib install-dev" % get.installDIR())

    pisitools.remove("/lib/*.a")
    shelltools.chmod("%s/lib/libattr.so.*.*.*" % get.installDIR(), 0755)
