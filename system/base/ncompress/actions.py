#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.move("Makefile.def", "Makefile")
    pisitools.dosed("Makefile","options= ","options= $(CFLAGS) -DNOFUNCDEF -DUTIME_H $(LDFLAGS) ")

def build():
    autotools.make()

def install():
    pisitools.dobin("compress")
    pisitools.dosym("compress", "/usr/bin/uncompress")

    pisitools.doman("compress.1")
