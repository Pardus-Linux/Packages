#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-nls \
                         --disable-java \
                         --disable-csharp \
                         --disable-rpath \
                         --disable-gtk-doc \
                         --disable-static")

def build():
    autotools.make()

def check():
    autotools.make("-C tests check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "FAQ", "NEWS", "README", "THANKS", "TODO")
