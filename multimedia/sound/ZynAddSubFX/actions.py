#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

shelltools.export("HOME", get.workDIR())

def build():
    shelltools.cd("src")
    autotools.make("-j1 CXX=%s" % get.CXX())
    shelltools.cd("../ExternalPrograms/Spliter")
    autotools.make("-j1 CXX=%s" % get.CXX())
    shelltools.cd("../Controller")
    autotools.make('-j1 CXX=%s CXXFLAGS="%s"' % (get.CXX(), get.CXXFLAGS()))

def install():
    pisitools.dobin("src/zynaddsubfx")
    pisitools.dobin("ExternalPrograms/Spliter/spliter")
    pisitools.dobin("ExternalPrograms/Controller/controller")

    pisitools.insinto("%s/%s" % (get.dataDIR(), get.srcNAME()), "banks")

    pisitools.dodoc("*.txt", "COPYING", "ChangeLog")
