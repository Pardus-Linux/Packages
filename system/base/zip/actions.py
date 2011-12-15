#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="%s30" % get.srcNAME()

def build():
    autotools.make('-f unix/Makefile CC="%s" CFLAGS_NOOPT="-I. -DUNIX %s" generic_gcc' % (get.CC(), get.CFLAGS()))

def install():
    autotools.rawInstall("-f unix/Makefile prefix=%s/usr MANDIR=%s/usr/share/man/man1" % (get.installDIR(), get.installDIR()))

    pisitools.dodoc("BUGS", "CHANGES", "LICENSE", "README", "TODO", "WHATSNEW", "WHERE")
