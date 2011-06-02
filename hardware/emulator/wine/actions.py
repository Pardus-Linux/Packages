# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-vif")
    options = "--without-capi \
               --with-curses \
               --without-esd \
               --with-opengl \
               --with-pulse \
               --with-x"

    if get.buildTYPE() == "emul32":
        options += "--libdir=/usr/lib32 \
                    --with-wine64=%s/work/%s" % (get.pkgDIR(), get.srcDIR())
    elif get.ARCH() == "x86_64":
        options += " --enable-win64"

    autotools.configure(options)

def build():
    autotools.make()

def install():
    if get.buildTYPE() == "emul32":
        autotools.install("UPDATE_DESKTOP_DATABASE=/bin/true libdir=%s/usr/lib32 dlldir=%s/usr/lib32/wine" % (get.installDIR(), get.installDIR()))
    else:
        autotools.install("UPDATE_DESKTOP_DATABASE=/bin/true libdir=%s/usr/lib dlldir=%s/usr/lib/wine" % (get.installDIR(), get.installDIR()))

    pisitools.dodoc("ANNOUNCE", "AUTHORS", "COPYING.LIB", "LICENSE*", "README", "documentation/README.*")
