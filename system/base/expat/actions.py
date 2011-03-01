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

cflags = "%s -fPIC" % get.CFLAGS()

def setup():
    options = "--disable-static"

    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32"
        cflags += " -m32"

    shelltools.export("CFLAGS", cflags)
    autotools.configure(options)

def build():
    autotools.make("-j1")

def check():
    autotools.make("check")

def install():
    autotools.rawInstall('DESTDIR=%s man1dir=/usr/share/man/man1' % get.installDIR())

    pisitools.dohtml("doc/*")
    pisitools.dodoc("Changes", "README")
