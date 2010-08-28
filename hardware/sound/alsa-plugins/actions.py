#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

if "_" in get.srcVERSION():
    WorkDir = get.srcNAME()

def setup():
    autotools.autoreconf("-fi")
    libtools.libtoolize()

    autotools.configure("--disable-static \
                         --enable-avcodec \
                         --enable-jack \
                         --enable-samplerate \
                         --enable-pulseaudio \
                         --with-speex=lib \
                         --disable-dependency-tracking")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("COPYING", "COPYING.GPL", "doc/*.txt", "doc/README*")
