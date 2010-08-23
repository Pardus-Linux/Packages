#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

# .la files needed to load modules
KeepSpecial = ["libtool"]

def setup():
    pisitools.dosed("configure.ac", "AC_PREREQ\(2.64\)", "AC_PREREQ(2.63)")
    autotools.autoreconf("-vif")

    # ghostscript is better than dps
    # unstable fpx support disabled
    # trio is for old systems not providing vsnprintf
    # FIXME: build perl modules
    autotools.configure("--enable-openmp \
                         --enable-shared \
                         --disable-static \
                         --with-threads \
                         --with-modules \
                         --with-magick-plus-plus \
                         --without-perl \
                         --with-bzlib \
                         --without-dps \
                         --without-fpx \
                         --with-gslib \
                         --with-jbig \
                         --with-jpeg \
                         --with-jp2 \
                         --with-lcms \
                         --with-png \
                         --with-tiff \
                         --without-trio \
                         --with-ttf \
                         --with-wmf \
                         --with-fontpath=/usr/share/fonts \
                         --with-gs-font-dir=/usr/share/fonts/default/ghostscript \
                         --with-xml \
                         --with-zlib \
                         --with-x")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/lib/*.la")
