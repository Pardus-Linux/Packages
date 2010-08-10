# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoreconf("-vif")
    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    # This library is deprecated. Make its usage hard.
    pisitools.rename("/usr/lib/libXp.so", "libdeprecatedXp.so")
    pisitools.removeDir("/usr/lib/pkgconfig")
    pisitools.removeDir("/usr/share")
