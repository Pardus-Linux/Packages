#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir = "broadcom-wl-%s" % get.srcVERSION()

def install():
    pisitools.dodir("/lib/firmware")
    shelltools.system("b43-fwcutter -w %s/lib/firmware driver/wl_apsta_mimo.o" % get.installDIR())
