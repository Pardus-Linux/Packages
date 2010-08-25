#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "SDL_gfx-%s" % get.srcVERSION()

def setup():
    pisitools.dosed("configure.in", "-O")
    shelltools.makedirs("m4")

    autotools.autoreconf("-vfi")
    autotools.configure("--disable-dependency-tracking \
                         --enable-mmx \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "LICENSE", "README")
    pisitools.insinto("/%s/sdl-gfx/" % get.docDIR(), "Docs", "html")
