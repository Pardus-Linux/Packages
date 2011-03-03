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

WorkDir = "talloc-%s" % get.srcVERSION()
libdir = "lib32" if get.buildTYPE() == "emul32" else "lib"

def setup():
    shelltools.system("./autogen.sh")

    options = "--enable-talloc-compat1"

    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32"
        shelltools.export("CC", "%s -m32" % get.CC())

    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/swig")

    pisitools.remove("/usr/lib*/*.a")
    pisitools.remove("/usr/lib*/libtalloc-compat1-%s.so" % get.srcVERSION())

    # Create symlinks for so file
    pisitools.dosym("libtalloc.so.%s" % get.srcVERSION(), "/usr/%s/libtalloc.so.%s" % (libdir, get.srcVERSION().split(".")[0]))
    pisitools.dosym("libtalloc.so.%s" % get.srcVERSION(), "/usr/%s/libtalloc.so" % libdir)

    pisitools.dodoc("NEWS")
