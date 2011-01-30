#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="nvclock0.8b4"

def setup():
    autotools.configure("--disable-gtk --disable-qt")

def build():
    autotools.make("-j1")

def install():
    pisitools.doman("nvclock.1")

    pisitools.dobin("src/nvclock")
    pisitools.dobin("src/smartdimmer")

    pisitools.dodoc("COPYING", "README", "ABOUT", "AUTHORS", "ChangeLog", "NEWS", "FAQ")
