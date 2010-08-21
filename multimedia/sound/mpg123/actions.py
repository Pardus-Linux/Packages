# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#This package using ltdl. .la files should be deleted only for plugins
KeepSpecial = ["libtool"]

def setup():
    cpu = "x86-64" if get.ARCH() == "x86_64" else "sse"

    pisitools.dosed("configure", "-faltivec")
    autotools.configure('--with-audio="alsa oss" \
                         --with-cpu=%s \
                         --with-optimization=2 \
                         --enable-network=yes \
                         --disable-ltdl-install' % cpu)

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("ChangeLog", "COPYING", "NEWS", "README", "AUTHORS")

    pisitools.remove("/usr/lib/libmpg123.la")
