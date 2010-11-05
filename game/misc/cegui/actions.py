#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "CEGUI-%s" % get.srcVERSION()

def setup():
    pisitools.touch("NEWS")
    autotools.autoreconf("-vfi")
    autotools.configure("--enable-xerces-c \
                         --enable-libxml \
                         --enable-expat \
                         --enable-tinyxml \
                         --enable-opengl-renderer \
                         --enable-tga \
                         --disable-samples \
                         --enable-toluacegui \
                         --with-x \
                         --with-gtk2 \
                         --enable-freeimage \
                         --disable-devil \
                         --enable-lua-module \
                         --disable-samples")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("ReadMe.html")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "TinyXML-License", "README", "TODO")
