# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    options = "--disable-static \
               --disable-docs \
               --with-cache-dir=/var/cache/fontconfig \
               --with-default-fonts=/usr/share/fonts \
               --with-add-fonts=/usr/local/share/fonts"

    # Do not rebuild docs
    shelltools.export("HASDOCBOOK", "no")

    if get.buildTYPE() == "emul32":
        options += " --prefix=/emul32 \
                     --libdir=/usr/lib32"
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
        shelltools.export("CXXFLAGS", "%s -m32" % get.CXXFLAGS())

    autotools.autoreconf("-vif")
    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    if get.buildTYPE():
        pisitools.removeDir("/emul32")
        return

    pisitools.insinto("/etc/fonts", "fonts.conf", "fonts.conf.new")

    enabled_configs = ("10-sub-pixel-rgb.conf", "70-yes-bitmaps.conf")
    disabled_configs = ("10-no-sub-pixel.conf",)

    for cfg in enabled_configs:
        pisitools.dosym("../conf.avail/%s" % cfg, "/etc/fonts/conf.d/%s" % cfg)

    for cfg in disabled_configs:
        pisitools.remove("/etc/fonts/conf.d/%s" % cfg)

    for i in ["fc-cat", "fc-list", "fc-match", "fc-cache"]:
        pisitools.doman("%s/*.1" % i)

    pisitools.doman("doc/*.3")

    pisitools.dodoc("AUTHORS", "COPYING", "README", "doc/*.txt")
