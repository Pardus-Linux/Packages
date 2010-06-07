#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS", "%s -D_GNU_SOURCE" % get.CFLAGS())

    autotools.configure("--enable-nls \
                         --without-internal-regex \
                         --disable-rpath \
                         --disable-assert \
                         --enable-d_type-optimization")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.install()

    pisitools.dodoc("ChangeLog", "NEWS", "TODO", "README")
