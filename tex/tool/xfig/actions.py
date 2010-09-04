#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir='xfig.%s' % get.srcVERSION()

def build():
    shelltools.system("xmkmf")
    autotools.make('-j1 CC="%s" LOCAL_LDFLAGS="%s" CDEBUGFLAGS="%s" USRLIBDIR=/usr/lib' % (get.CC(), get.LDFLAGS(), get.CFLAGS()))

def install():
    autotools.make('DESTDIR=%s \
                    MANDIR=/usr/share/man/man1 \
                    MANSUFFIX=1 \
                    install install.all' % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps", "xfig.png")
    pisitools.removeDir("/etc")
