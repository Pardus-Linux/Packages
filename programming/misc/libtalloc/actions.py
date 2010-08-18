#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "talloc-%s" % get.srcVERSION()

def setup():
    shelltools.system("./autogen.sh")
    autotools.configure("--enable-talloc-compat1")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/lib/*.a")
    pisitools.remove("/usr/lib/libtalloc-compat1-%s.so" % get.srcVERSION())

    # Create symlinks for so file
    pisitools.dosym("libtalloc.so.%s" % get.srcVERSION(), "/usr/lib/libtalloc.so.%s" % get.srcVERSION().split(".")[0])
    pisitools.dosym("libtalloc.so.%s" % get.srcVERSION(), "/usr/lib/libtalloc.so")

    pisitools.removeDir("/usr/share/swig")

    pisitools.dodoc("NEWS")
