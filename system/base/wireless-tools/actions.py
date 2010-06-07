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

WorkDir="wireless_tools.29"

def setup():
    pisitools.dosed("Makefile", "CC = .*", "CC = %s" % get.CC())
    pisitools.dosed("Makefile", "^CFLAGS=", "CFLAGS=%s " % get.CFLAGS())

def build():
    autotools.make()

def install():
    autotools.rawInstall("PREFIX=%s/usr INSTALL_INC=%s/usr/include INSTALL_MAN=%s/usr/share/man" % (get.installDIR(), get.installDIR(), get.installDIR()))
    pisitools.dosym("/usr/sbin/iwlist", "/usr/bin/iwlist")

    pisitools.dodoc("CHANGELOG.h", "COPYING", "HOTPLUG.txt", "IFRENAME-VS-XXX.txt", "PCMCIA.txt", "README")
