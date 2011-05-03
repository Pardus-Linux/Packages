#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    autotools.autoreconf("-fi")
    # don't remove --with-debugger as it is needed for reverse dependencies
    options = "--with-python \
               --with-crypto \
               --with-debugger \
               --disable-static"

    if get.buildTYPE() == "emul32":
        options += " --prefix=/emul32 \
                     --without-python \
                     --libdir=/usr/lib32"
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())

    autotools.configure(options)

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "emul32":
        pisitools.removeDir("/emul32")
        return

    pisitools.dodoc("AUTHORS", "ChangeLog", "Copyright", "FEATURES", "NEWS", "README", "TODO")
