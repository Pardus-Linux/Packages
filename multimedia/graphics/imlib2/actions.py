#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

optimizationtype = "--enable-amd64" if get.ARCH() == "x86_64" else "--enable-mmx"

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--disable-static \
                         --with-x \
                         --with-jpeg \
                         --with-png \
                         --with-tiff \
                         --with-gif \
                         --with-zlib \
                         --with-bzip2 \
                         --with-id3 \
                         %s \
                         --enable-visibility-hiding" % optimizationtype)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("doc/*")
    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "TODO")
