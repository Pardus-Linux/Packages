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
    autotools.autoreconf("-fi")
    pisitools.dosed("po/Makefile.*", "@MKINSTALLDIRS@", "%s/mkinstalldirs" % get.curDIR())

    autotools.configure("--disable-gdkpixbuf-plugin \
                         --disable-infinite \
                         --disable-jack \
                         --disable-esd \
                         --disable-rpath \
                         --enable-extra-optimization")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "NEWS", "TODO", "README", "AUTHORS")
