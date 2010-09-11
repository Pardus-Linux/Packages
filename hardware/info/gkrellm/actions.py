#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    for d in ["po", "server", "src"]:
        pisitools.dosed("%s/Makefile" % d, "-O2")
        pisitools.dosed("%s/Makefile" % d, "override CC", "CFLAGS")

def build():
    autotools.make('CC=%s \
                    INSTALLROOT=/usr \
                    INCLUDEDIR=/usr/include/gkrellm2 \
                    LOCALEDIR=/usr/share/locale \
                    STRIP="" \
                    LINK_FLAGS="%s -Wl,-E" \
                    enable_nls=1 \
                    without-ssl=yes \
                    without-sensors=no \
                    without-libsensors=yes' % (get.CC(), get.LDFLAGS()))
                    # without ssl option enables gnutls

def install():
    autotools.rawInstall("DESTDIR=%s \
                          PREFIX=/usr" % get.installDIR())

    pisitools.insinto("/etc", "server/gkrellmd.conf")

    pisitools.doman("gkrellm.1")
    pisitools.doman("gkrellmd.1")

    pisitools.dodoc("CREDITS", "README", "Changelog", "COPYRIGHT")
    pisitools.dohtml("*")


