#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("configure.ac", "-mfpmath=387", "")
    autotools.autoreconf("-fi")

    # disable libpng because it's only used for tests
    autotools.configure("--disable-libpng \
                         --disable-dependency-tracking \
                         --without-cpuflags \
                         --without-doxygen")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
