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
    autotools.configure("--datadir=/usr/share/misc \
                         --disable-zlib")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/sbin/update-usbids.sh")
    pisitools.dodir("/usr/share/pkgconfig")
    pisitools.domove("/usr/share/misc/pkgconfig/*.pc", "/usr/share/pkgconfig/")
    pisitools.removeDir("/usr/share/misc/pkgconfig")

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
