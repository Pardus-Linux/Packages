#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def setup():
    options = "--disable-static \
               --enable-silent-rules \
               --enable-introspection \
               --with-libjasper \
               --with-included-loaders=png"

    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32 \
                     --bindir=/emul32/bin"

        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())

    autotools.autoreconf("-fiv")

    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        pisitools.removeDir("emul32")

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README")
