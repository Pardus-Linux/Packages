#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "SDL_mixer-%s" % get.srcVERSION()

def setup():
    pisitools.dosed("timidity/config.h", "/usr/local/lib/timidity", "/usr/share/timidity")

    autotools.configure("--disable-dependency-tracking \
                         --disable-static \
                         --enable-music-midi \
                         --enable-timidity-midi \
                         --enable-music-mod \
                         --enable-music-libmikmod \
                         --enable-music-mp3 \
                         --enable-music-ogg")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("CHANGES", "COPYING", "README")
