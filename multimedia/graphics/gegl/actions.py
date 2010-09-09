#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    pisitools.dosed("docs/Makefile.in", "share/gtk-doc/html/gegl", "share/doc/%s/html" % get.srcNAME())
    autotools.configure("--enable-mmx \
                         --enable-sse \
                         --with-cairo \
                         --with-graphviz \
                         --with-gtk \
                         --with-gdk-pixbuf \
                         --with-libjpeg \
                         --with-libopenraw \
                         --with-libpng \
                         --with-librsvg \
                         --with-libspiro \
                         --with-libv4l \
                         --with-lua \
                         --with-openexr \
                         --with-pango \
                         --with-pangocairo \
                         --with-sdl \
                         --disable-static \
                         --disable-gtk-doc \
                         --enable-workshop")

    # libtool fixes for underlinking problems
    for op in ["affine", "core", "common", "external", "generated", "workshop/generated", "workshop/external", "workshop"]:
        pisitools.dosed("operations/%s/Makefile" % op, "^#(libgegl.*)$", "\\1")
        pisitools.dosed("operations/%s/Makefile" % op, "^AVFORMAT_LIBS = (.*)$", "AVFORMAT_LIBS = \\1 -lavutil")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "COPYING.LESSER", "NEWS", "README")

