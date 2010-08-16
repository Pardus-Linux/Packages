#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="ntfs-3g-%s" % get.srcVERSION()[4:]

def setup():
    shelltools.export("CFLAGS", "%s -D_FILE_OFFSET_BITS=64" % get.CFLAGS())
    autotools.configure("--exec-prefix=/ \
                         --bindir=/bin \
                         --sbindir=/sbin \
                         --libdir=/usr/lib \
                         --disable-static \
                         --disable-ldconfig \
                         --with-fuse=external \
                         --docdir=/usr/share/doc/%s" % get.srcNAME())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/lib/pkgconfig", "libntfs-3g/*.pc")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "CREDITS", "NEWS", "README")
