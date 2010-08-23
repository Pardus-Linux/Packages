#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# licensed under the gnu general public license, version 2.
# see the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "notification-%s" % get.srcVERSION()

def setup():
    shelltools.export("AUTOPOINT", "/bin/true")

    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING*", "README")
