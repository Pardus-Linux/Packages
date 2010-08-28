#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile.in", "xmlto man", "xmlto --skip-validation man")
    pisitools.dosed("Makefile.in", "udevrulesdir = .*$", "udevrulesdir = /lib/udev/rules.d")
    pisitools.dosed("Makefile.in", "udevhelperdir = .*$", "udevhelperdir = /lib/udev")

    autotools.configure("--with-udev-rules \
                         --disable-rpath")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/var/run/udev-configure-printer")

    pisitools.dodoc("README", "AUTHORS", "NEWS", "COPYING", "ChangeLog")
