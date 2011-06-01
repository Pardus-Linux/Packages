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

    if get.buildTYPE() == "emul32":
        autotools.configure("--without-capi \
                             --with-curses \
                             --without-esd \
                             --with-opengl \
                             --with-pulse \
                             --with-x \
                             --libdir=/usr/lib32 \
                             --with-wine64=%s/work/%s" % (get.pkgDIR(), get.srcDIR()))
    else:
        args = ""
        if get.ARCH() == "x86_64":
            args = " --enable-win64"

        autotools.configure("--without-capi \
                             --with-curses \
                             --without-esd \
                             --with-opengl \
                             --with-pulse \
                             --with-x \
                             %s" % args)


def build():
    autotools.make()

def install():
    if get.buildTYPE() == "emul32":
        autotools.install("UPDATE_DESKTOP_DATABASE=/bin/true libdir=%s/usr/lib32 dlldir=%s/usr/lib32/wine" % (get.installDIR(), get.installDIR()))
    else:
        autotools.install("UPDATE_DESKTOP_DATABASE=/bin/true libdir=%s/usr/lib dlldir=%s/usr/lib/wine" % (get.installDIR(), get.installDIR()))

    pisitools.dodoc("ANNOUNCE", "AUTHORS", "COPYING.LIB", "LICENSE*", "README", "documentation/README.*")
