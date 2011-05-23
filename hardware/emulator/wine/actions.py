# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    autotools.autoreconf("-vif")

    options = "--without-capi \
               --without-esd \
               --with-opengl \
               --with-x \
               --with-pulse \
               --mandir=%s/usr/share/man" % get.installDIR()

    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32"

        shelltools.export("CC", "%s -m32" % get.CC())
        shelltools.export("LDFLAGS", "%s -m32" % get.LDFLAGS())
        shelltools.export("PKG_CONFIG_PATH", "/usr/lib32/pkgconfig")

    autotools.configure(options)

def build():
    autotools.make()

def install():
    if get.buildTYPE() == "emul32":
        autotools.rawInstall("libdir=%s/usr/lib32 dlldir=%s/usr/lib32/wine" % (get.installDIR(), get.installDIR()))
        return

    # Wine prefixes are buggy, we have to define all exclusively
    autotools.rawInstall("DESTDIR=/ prefix=%s/usr includedir=%s/usr/include/wine libdir=%s/usr/lib dlldir=%s/usr/lib/wine datadir=%s/usr/share UPDATE_DESKTOP_DATABASE=/bin/true" % (get.installDIR(), get.installDIR(), get.installDIR(), get.installDIR(), get.installDIR()))

    pisitools.dodoc("ANNOUNCE", "AUTHORS", "COPYING.LIB", "LICENSE*", "README", "documentation/README.*")
