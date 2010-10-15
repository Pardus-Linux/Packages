#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-udev \
                         --enable-twinserial \
                         --disable-static \
                         --disable-dependency-tracking")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/lib/udev/rules.d/", "src/pcscd_ccid.rules", "85-pcscd_ccid.rules")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
