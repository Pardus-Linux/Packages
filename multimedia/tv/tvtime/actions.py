#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS","%s -fPIC" % get.CFLAGS())
    autotools.autoreconf("-vfi")
    autotools.configure("--enable-nls \
                         --with-xinerama")

def build():
    autotools.make()
    shelltools.cd("po")
    autotools.make("update-po")

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    # We will use our desktop file
    pisitools.remove("/usr/share/applications/net-tvtime.desktop")

    pisitools.dohtml("docs/html/*")
    pisitools.dodoc("ChangeLog", "AUTHORS", "NEWS", "README")
