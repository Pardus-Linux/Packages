#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools

def setup():
    autotools.autoreconf("-vfi")
    shelltools.system("intltoolize --copy --force")

    shelltools.export("PTHREAD_LIBS", "-lpthread")

    autotools.configure("--without-forced-embedded-ffmpeg \
                         --with-x \
                         --enable-libtheora \
                         --enable-libmp3lame")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc( "ChangeLog", "COPYING", "AUTHORS", "NEWS", "README")
