#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir = "zd1211-firmware"

def setup():
    pass


def build():
    autotools.make("CFLAGS='%s'" % get.CFLAGS())

def install():
    autotools.install("FW_DIR=%s/lib/firmware/zd1211" % get.installDIR())

    pisitools.dodoc("README", "COPYING")
