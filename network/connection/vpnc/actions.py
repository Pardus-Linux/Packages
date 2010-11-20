#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make('CC="%s" CFLAGS="%s -fPIE" LDFLAGS="%s -pie -lgcrypt"' % (get.CC(),
                                                                             get.CFLAGS(),
                                                                             get.LDFLAGS()))

def install():
    autotools.rawInstall("DESTDIR=%s PREFIX=/usr" % get.installDIR())

    pisitools.dodir("/var/run/vpnc")

    pisitools.dodoc("README")
