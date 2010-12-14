#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


data = "/usr/share/%s/" % get.srcNAME()
WorkDir = "starfighter-%s" % get.srcVERSION()

def setup():
    pisitools.dosed("makefile", "-O3", get.CXXFLAGS())
    pisitools.dosed("makefile", "^DATADIR =.*", "DATADIR = %s" % data)

def build():
    autotools.make()

def install():
    pisitools.dobin("starfighter")
    pisitools.insinto(data, "starfighter.pak")
    pisitools.dohtml("docs/")
