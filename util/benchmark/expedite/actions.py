#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-simple-x11 \
                         --enable-software-x11 \
                         --enable-xrender-x11 \
                         --enable-opengl-x11 \
                         --enable-xrender-xcb \
                         --enable-opengl-glew \
                         --enable-software-sdl \
                         --enable-opengl-sdl \
                         --enable-fb \
                         --enable-directfb \
                         --enable-software-16-x11")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps", "data/e.png", "expedite.png")

    pisitools.dodoc("AUTHORS", "COPYING", "README")
