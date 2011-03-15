#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "libaesgm-%s" % get.srcVERSION().split("_", 1)[1]

def setup():
    pisitools.dosed("*.txt", "\r")

def build():
    autotools.make('CFLAGS="%s -fPIC -DUSE_SHA1"' % get.CFLAGS())

def install():
    autotools.rawInstall("DESTDIR=%s LIBDIR=/usr/lib" % get.installDIR())

    pisitools.dodoc("*.txt", "*.doc")

