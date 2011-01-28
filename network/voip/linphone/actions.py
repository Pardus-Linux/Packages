#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("CFLAGS", get.CFLAGS().replace("-D_FORTIFY_SOURCE=2", ""))

def setup():
    autotools.autoreconf("-vfi")
    shelltools.cd("mediastreamer2")
    autotools.autoreconf("-vfi")
    shelltools.cd("..")
    autotools.configure("--enable-shared \
                         --disable-static \
                         --enable-external-ortp \
                         --enable-ipv6 \
                         --enable-alsa \
                         --disable-rpath")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/gnome")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO")
