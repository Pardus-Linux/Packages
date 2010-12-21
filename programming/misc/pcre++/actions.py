#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # use CXXFLAGS from environment
    pisitools.dosed("libpcre++/Makefile.am", "^CXXFLAGS.*", "")
    autotools.autoreconf("-fi")

    autotools.configure("--disable-static")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("%s/usr/doc/libpcre++-%s/*" % (get.installDIR(),get.srcVERSION()))
    pisitools.removeDir("/usr/doc")
