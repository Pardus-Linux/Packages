#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--disable-static \
                         --with-jpeg \
                         --with-libtiff=/usr/include \
                         --with-proj \
                         --with-zip")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dobin("bin/makegeo")

    # pisitools.remove("/usr/lib/libgeotiff.a")

    pisitools.dodoc("README", "LICENSE")
