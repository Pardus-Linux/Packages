#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-shared \
                         --disable-static \
                         --enable-maxmem=64")

def build():
    autotools.make()

def install():
    # create needed diretories for install
    pisitools.dodir("/usr/include")
    pisitools.dodir("/usr/lib")
    pisitools.dodir("/usr/bin")
    pisitools.dodir("/usr/share/man/man1")

    autotools.rawInstall("prefix=%s/usr libdir=%s/usr/lib mandir=%s/usr/share/man/man1" % (get.installDIR(), get.installDIR(), get.installDIR()))

    pisitools.insinto("/usr/include", "jpegint.h")
    pisitools.insinto("/usr/include", "jinclude.h")

    pisitools.dodoc("README", "install.doc", "usage.doc", "wizard.doc", "change.log", "libjpeg.doc", "example.c", "structure.doc", "filelist.doc", "coderules.doc")
