#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="ftgl-%s" % get.srcVERSION().replace("_", "~")

def setup():
    autotools.autoreconf("-vfi")
    autotools.configure("--enable-shared \
                         --disable-static")
def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "NEWS", "README", "TODO")

