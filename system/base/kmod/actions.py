# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-static --with-xz --with-zlib")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodir("/etc/modprobe.d")
    pisitools.dodir("/etc/depmod.d")
    pisitools.dodir("/lib/modprobe.d")

    pisitools.dodoc("COPYING", "README")
