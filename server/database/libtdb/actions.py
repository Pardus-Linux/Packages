#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "tdb-%s" % get.srcVERSION()

def setup():
    #autotools.autoreconf("-fi")
    #autotools.autoconf()
    shelltools.system("./autogen.sh")
    autotools.configure("--enable-python")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.remove("/usr/lib/*.a")

    pisitools.dodoc("docs/README")
