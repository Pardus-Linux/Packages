# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

wine64 = get.ARCH() == "x86_64"

def setup():
    autotools.autoreconf("-vif")

    if wine64:
        shelltools.makedirs("build-wow64")
        shelltools.sym("../configure", "build-wow64/configure")

    shelltools.makedirs("build")
    shelltools.sym("../configure", "build/configure")

    shelltools.cd("build")
    args = "--enable-win64" if wine64 else ""
    autotools.configure("--without-capi \
                         --with-curses \
                         --without-esd \
                         --with-opengl \
                         --with-pulse \
                         %s" % args)

def build():
    autotools.make("-C build")

    if wine64:
        shelltools.cd("build-wow64")
        autotools.configure("--without-capi \
                             --with-curses \
                             --without-esd \
                             --with-opengl \
                             --with-pulse \
                             --with-wine64=../build")

        autotools.make()


def install():
    autotools.install("-C build UPDATE_DESKTOP_DATABASE=/bin/true")

    if wine64:
        autotools.install("-C build-wow64 UPDATE_DESKTOP_DATABASE=/bin/true")

    pisitools.dodoc("ANNOUNCE", "AUTHORS", "COPYING.LIB", "LICENSE*", "README", "documentation/README.*")
