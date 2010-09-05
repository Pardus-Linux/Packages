#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

NoStrip = ["/"]
WorkDir = "."

datafile_intel = "microcode-20100826.dat"
datafile_amd = "amd-ucode-2009-10-09/microcode_amd.bin"

def setup():
    shelltools.chmod(datafile_intel, 0644)
    shelltools.chmod(datafile_amd, 0644)

def install():
    pisitools.insinto("/lib/firmware", datafile_intel, "microcode.dat")
    pisitools.insinto("/lib/firmware/amd-ucode/", datafile_amd)

