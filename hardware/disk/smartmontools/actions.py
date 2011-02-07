#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    shelltools.touch("ChangeLog")
    autotools.autoreconf("-fi")
    autotools.configure("--with-libcap-ng=yes")

def build():
    autotools.make("CXXFLAGS='%s -fpie'" % get.CXXFLAGS())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #pisitools.insinto("/etc/", "smartd.conf")

    pisitools.removeDir("/etc/rc.d")

    pisitools.dodoc("AUTHORS", "NEWS", "README", "WARNINGS", "smartd.conf")
