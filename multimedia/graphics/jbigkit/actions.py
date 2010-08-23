#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="jbigkit"

def build():
    autotools.make("CC=%s CFLAGS='%s'" % (get.CC(), get.CFLAGS()))

def check():
    autotools.make("test")

def install():
    autotools.rawInstall("DESTDIR=%s prefix=/usr libdir=/usr/lib" % get.installDIR())

    pisitools.doman("pbmtools/jbgtopbm.1", "pbmtools/pbmtojbg.1")
    pisitools.dodoc("ANNOUNCE", "CHANGES", "COPYING", "TODO")
