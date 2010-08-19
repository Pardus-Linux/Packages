#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoconf()

    autotools.configure("--with-pic \
                         --enable-ogg \
                         --enable-sse \
                         --disable-doxygen-docs \
                         --disable-dependency-tracking \
                         --disable-xmms-plugin \
                         --disable-static")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/doc/")

    pisitools.dohtml("doc/html/*")
