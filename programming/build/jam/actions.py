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

def build():
    shelltools.export("PATH", "%s:%s" % (get.curDIR(), get.ENV("PATH")))
    shelltools.export("CFLAGS", "%s -fno-strict-aliasing" % get.CFLAGS())

    autotools.make('-j1 YACC="bison -y" CFLAGS="%s" CC="%s"' % (get.CFLAGS(), get.CC()))

def install():
    shelltools.export("PATH", "%s:%s" % (get.curDIR(), get.ENV("PATH")))
    shelltools.export("BINDIR", "%s/usr/bin" % get.installDIR())
    shelltools.system("./jam0 install")

    pisitools.dohtml("Jam.html", "Jambase.html", "Jamfile.html")
    pisitools.dodoc("README", "RELNOTES", "Porting")
