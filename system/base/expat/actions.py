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
    autotools.configure("--disable-static")

def build():
    autotools.make("-j1")

def check():
    autotools.make("check")

def install():
    autotools.install('man1dir="%s/usr/share/man/man1"' % get.installDIR())

    pisitools.dohtml("doc/*")
    pisitools.dodoc("Changes", "README")
