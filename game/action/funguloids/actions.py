#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "funguloids-1.06-4"

def setup():
    #shelltools.export("CXXFLAGS", "%s -Wno-deprecated" % get.CXXFLAGS())

    shelltools.cd("funguloids")
    autotools.autoreconf("-fi")

    autotools.configure("--without-fmod \
                         --with-openal \
                         --with-ogg \
                         --with-mad")

def build():
    shelltools.cd("funguloids")
    autotools.make()

def install():
    shelltools.cd("funguloids")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.rename("/usr/share/docs", "doc")
    pisitools.dodoc("COPYING", "README")
