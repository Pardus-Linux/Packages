#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="%s%s" % (get.srcNAME(), get.srcVERSION().replace(".",""))

def build():
    autotools.make('-f unix/Makefile CC="%s" CF_NOOPT="%s -I. -D_FILE_OFFSET_BITS=64 -DUNIX" generic_gcc' % (get.CC(), get.CFLAGS()))

def install():
    autotools.rawInstall("-f unix/Makefile prefix=%s/usr MANDIR=%s/usr/share/man/man1 INSTALL='cp -p'" % (get.installDIR(), get.installDIR()))

    pisitools.dodoc("BUGS", "History*", "LICENSE", "README", "ToDo", "WHERE")
