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
    options = "--libdir=/usr/lib \
               --includedir=/usr/include \
               --prefix=/usr"

    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32"
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())

    autotools.rawConfigure(options)

def build():
    autotools.make()

def check():
    autotools.make("-j1 test")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/lib*/*.a")

    if get.buildTYPE():
        return

    pisitools.doman("zlib.3")
    pisitools.dodoc("FAQ", "README", "ChangeLog", "doc/algorithm.txt", "example.c")


if get.buildTYPE() == "minizip":
    minizip_dir = "contrib/minizip"

    def setup():
        shelltools.copy("minigzip.c", minizip_dir)
        shelltools.cd(minizip_dir)
        shelltools.makedirs("m4")

        autotools.autoreconf("-vif")
        autotools.configure()

    def build():
        autotools.make("-C %s" % minizip_dir)

    def check():
        pass

    def install():
        autotools.rawInstall("-C %s DESTDIR=%s" % (minizip_dir, get.installDIR()))
