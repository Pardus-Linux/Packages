#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools

WorkDir = "AstroMenaceSourceCode"

def setup():
    cmaketools.configure("-DDATADIR=/usr/share/AstroMenace")

def build():
    cmaketools.make()

def install():
    pisitools.dobin("AstroMenace")

    pisitools.dodoc("gpl-3.0.txt", "License.txt", "ReadMe.txt")
