#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-nls \
                         --bindir=/bin \
                         --with-rmt=/usr/sbin/rmt")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/share/man/man1/mt.1")
    pisitools.removeDir("/usr/libexec")

    pisitools.dodoc("ChangeLog", "NEWS", "README")

def check():
    autotools.make("check")
