#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools

def setup():
    shelltools.export("AUTOPOINT", "true")
    autotools.autoreconf("-fi")

    autotools.configure("--disable-static \
                         --disable-rpath \
                         --disable-dependency-tracking \
                         --enable-guile \
                         --with-lzo \
                         --with-zlib \
                         --with-included-libcfg")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.install()

