#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    libtools.libtoolize("--force --install")
    autotools.autoreconf("-fi")

    options = "--with-x \
               --disable-gl \
               --disable-static"

    if get.buildTYPE() == "emul32":
        options += " --prefix=/emul32 \
                     --libdir=/usr/lib32"

        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())

    autotools.configure(options)

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/emul32")

    pisitools.dohtml("doc/")
    pisitools.dodoc("AUTHORS","BUGS","ChangeLog","NEWS","doc/*.txt")
