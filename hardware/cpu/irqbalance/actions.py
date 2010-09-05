#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    for f in ("NEWS", "AUTHORS", "README", "ChangeLog"):
        shelltools.touch("%s/%s" % (get.curDIR(), f))

    shelltools.chmod("%s/autogen.sh" % get.curDIR())
    shelltools.system("./autogen.sh")

    autotools.configure()
    pisitools.dosed("Makefile", "\-g.*\-Os ", "")

def build():
    autotools.make("CFLAGS='%s'" % get.CFLAGS())

def install():
    pisitools.dosbin("irqbalance")
