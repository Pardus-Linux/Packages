#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

SNAPSHOT="20101222"

def build():
    autotools.make("CC='%s' CFLAGS='%s'" % (get.CC(), get.CFLAGS()))

def install():
    autotools.rawInstall("DESTDIR='%s'" % get.installDIR())
    autotools.rawInstall("-C usb-modeswitch-data-%s DESTDIR='%s'" % (SNAPSHOT, get.installDIR()))

    pisitools.dodoc("README*", "COPYING")
