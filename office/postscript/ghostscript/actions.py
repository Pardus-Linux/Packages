#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # Remove local copies for system libs
    for directory in ["jpeg", "libpng", "zlib", "jasper", "expat"]:
        shelltools.unlinkDir(directory)

    shelltools.export("CFLAGS", "%s -fno-strict-aliasing" % get.CFLAGS())

    autotools.autoreconf("-fi")

    autotools.configure("--disable-compile-inits \
                         --disable-gtk \
                         --disable-cairo \
                         --enable-dynamic \
                         --enable-cups \
                         --with-system-libtiff \
                         --with-ijs \
                         --with-drivers=ALL \
                         --with-libpaper \
                         --with-jbig2dec \
                         --with-jasper \
                         --with-omni \
                         --with-x \
                         --with-fontpath=/usr/share/fonts:/usr/share/fonts/default/ghostscript:/usr/share/cups/fonts:/usr/share/fonts/TTF:/usr/share/fonts/Type1")

    shelltools.cd("ijs/")
    shelltools.system("./autogen.sh \
                       --prefix=/usr \
                       --mandir=/usr/share/man \
                       --disable-static \
                       --enable-shared")

def build():
    autotools.make("-C ijs")
    autotools.make("so")
    autotools.make()
    autotools.make("cups")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "soinstall")

    # For cjk stuff
    pisitools.dodir("/usr/share/ghostscript/Resource/Init")

    # Install missing header
    pisitools.insinto("/usr/include/ghostscript", "base/errors.h")

    # Install ijs
    autotools.rawInstall("-C ijs DESTDIR=%s" % get.installDIR())
    pisitools.removeDir("/usr/lib/pkgconfig")

    # Remove ijs examples
    pisitools.remove("/usr/bin/ijs_*_example")

    # Install docs
    pisitools.remove("/usr/share/doc/ghostscript/*.htm*")
    pisitools.remove("/usr/share/doc/ghostscript/*.css")

    pisitools.dohtml("doc/*")
    pisitools.dodoc("doc/AUTHORS", "doc/COPYING")
