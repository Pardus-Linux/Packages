#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "portaudio"

def setup():
    autotools.configure("--disable-static --enable-cxx")

def build():
    autotools.make()
    shelltools.system("doxygen")

def install():
    autotools.rawInstall('DESTDIR="%s" libdir=/usr/lib' % get.installDIR())

    pisitools.insinto("/%s/%s" % (get.docDIR(), get.srcNAME()), "doc/html")
    pisitools.dodoc("LICENSE.txt", "README.txt")
