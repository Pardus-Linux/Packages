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
    shelltools.export("CFLAGS","%s -fPIC" % get.CFLAGS())
    shelltools.export("AUTOPOINT", "true")

    autotools.autoreconf("-vfi")
    # do not enable nls http://bugs.gentoo.org/121408
    autotools.configure("--disable-nls \
                         --disable-dependency-tracking")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("flex", "/usr/bin/lex")

    pisitools.dodoc("NEWS", "README")
