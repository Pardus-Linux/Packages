#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fvi")
    autotools.configure("\
            --enable-ftdi-support \
            --enable-doc \
            --sysconfdir=/etc/avrdude" )

def build():
    autotools.make("-j1")

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS")
