#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    pisitools.dosed("Makefile", "CC =.*$", "CC = %s %s" % (get.CC(), get.CFLAGS()))
    autotools.make()

def install():
    pisitools.dobin("genus2reduction")

    pisitools.dodoc("CHANGES", "README")
