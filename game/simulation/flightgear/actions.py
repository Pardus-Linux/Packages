#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "FlightGear-%s" % get.srcVERSION()

def setup():
    autotools.configure("--enable-sp-fdms \
                         --with-threads \
                         --enable-sdl \
                         --with-x")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("README*", "ChangeLog", "AUTHORS", "NEWS", "Thanks")
